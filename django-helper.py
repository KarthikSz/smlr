'''from transcribe import amazon_transcribe

result=(amazon_transcribe(audio_file_name))
#include .mp4 while passing file name

from drop_box import dropbox_upload
dropbox_upload("Trump","Who is trump?")
print('processed') '''

from pipeline_creator import nlp
print(nlp( "Gravity (from Latin gravitas, meaning 'weight'), or gravitation, is a natural phenomenon by which all \
things with mass or energy—including planets, stars, galaxies, and even light—are brought toward (or gravitate toward) \
one another. On Earth, gravity gives weight to physical objects, and the Moon's gravity causes the ocean tides. \
The gravitational attraction of the original gaseous matter present in the Universe caused it to begin coalescing \
and forming stars and caused the stars to group together into galaxies, so gravity is responsible for many of \
the large-scale structures in the Universe. Gravity has an infinite range, although its effects become increasingly \
weaker as objects get further away"))