"""

- kulanıcıdan vize ve final notları alınır.
- not = vize * 0.4 + final * 0.6
çıktı
dönem sonu notu
"""

vize= int(input("vize notunu gir"))
final= int(input("final notunu gir"))

notunuz= vize*0.4 + final*0.6

print(" dönem sonu notun: {}".format(notunuz))