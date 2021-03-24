import os
from tempfile import TemporaryDirectory

import click
import toml
import ffmpeg
from gtts import gTTS


def gtts_generate(text, lang, output):
    tts = gTTS(text=text, lang=lang)
    tts.save(output)


def mp3_to_ogg(mp3_filename, ogg_filename):
    gen_input = ffmpeg.input(mp3_filename)
    ffmpeg.output(gen_input.audio, ogg_filename, acodec="libvorbis").run(quiet=True, overwrite_output=True)


@click.command(help="Generate audio files")
@click.option("-c", "--conf", help="Configuration", type=click.Path(exists=True), required=True)
@click.option("-o", "--output", "out_dirname", help="Input file",
              type=click.Path(exists=False, file_okay=False, dir_okay=True),
              required=True)
def cli(conf, out_dirname):
    with open(conf, "r") as f:
        conf = toml.load(f)

    lang = conf["info"]["language"]
    texts = conf["texts"]

    print("Generating audio files")

    if not os.path.exists(out_dirname):
        os.makedirs(out_dirname)

    with TemporaryDirectory() as tmp_dir:
        for (key, text) in texts.items():
            tts_output_filename = "{}/{}.mp3".format(tmp_dir, key)
            gtts_generate(text, lang, tts_output_filename)
            ogg_output_filename = "{}/{}.ogg".format(out_dirname, key)
            if os.path.exists(ogg_output_filename):
                print("Overwriting {}".format(ogg_output_filename))
            else:
                print("New file {}".format(ogg_output_filename))

            mp3_to_ogg(tts_output_filename, ogg_output_filename)