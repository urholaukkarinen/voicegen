# TTS voice generator script for Roborock S5 Max

This is a script that generates audio files from texts using google's text-to-speech api. Similar to https://github.com/dgiese/dustcloud/tree/master/devices/xiaomi.vacuum/audio_generator.

The script reads the texts used to generate the sound files from a toml file. See the `texts_en.toml` file for default english texts.

## How to use

Install dependencies with `pip install -r requirements.txt` and run the script with `python src/voicegen -c texts_en.toml -o output_dir`
 

## Additional notes

Voice files for S5 Max can be found in 
̉̉`/mnt/resources/audio_default` and `/mnt/resources/audio_custom`.

`/mnt/resources/audio_default` is mounted to `/dev/nandi` and 
`/mnt/resources/audio_custom` is mounted to `/dev/nandj`.
If you have changed the robot's voice to something other than the default voice, the audio_custom is used.


You can use the following commands to customize the voice **(USE AT YOUR OWN RISK)**:

S5 Max:
* `umount /dev/nandj`
* `dd if=/dev/nandj of=/tmp/sounds.sqfs`
* `mount /dev/nandj /mnt/resources/audio_custom`

PC:
* `scp root@robot_ip:/tmp/sounds.sqfs sounds.sqfs`
* `unsquashfs sounds.sqfs`
* `python src/voicegen -c texts_en.toml -o squashfs-root/sounds`
* `mksquashfs squashfs-root new_sounds.sqfs`
* `scp new_sounds.sqfs root@robot_ip:/tmp/sounds.sqfs`

S5 Max:
* `umount /dev/nandj`
* `dd if=/tmp/sounds.sqfs of=/dev/nandj`
* `mount /dev/nandj /mnt/resources/audio_custom`
