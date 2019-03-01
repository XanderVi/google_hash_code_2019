import random


class Photo:
    def __init__(self, id, orientation, tags):
        self.id = id
        self.orientation = orientation
        self.tags = tags

    def __repr__(self):
        return str(self.id) + " " + self.orientation + " " + "|".join(self.tags)


class Slide:
    def __init__(self, photo_1, photo_2):
        self.id = str(photo_1.id) + " " + str(photo_2.id)
        self.tags = list(set(photo_1.tags + photo_2.tags))


def create_photo(id, photo_info):
    photo_info = photo_info.split()
    return Photo(id, photo_info[0], photo_info[2:])


def score(slide_1, slide_2):
    tags_1 = slide_1.tags
    tags_2 = slide_2.tags
    all_tags = list(set(tags_1 + tags_2))
    result_1 = 0
    result_2 = 0
    result_3 = 0
    for tag in all_tags:
        if tag in tags_1 and tag in tags_2:
            result_1 += 1
        if tag in tags_1 and tag not in tags_2:
            result_2 += 1
        if tag in tags_2 and tag not in tags_1:
            result_3 += 1
    return min(result_1, result_2, result_3)


data = []
# Use 'a.txt', 'b.txt' and so on
info = open("inputs/c.txt", "r")
for line in info:
    data.append(line.replace("\n", ""))

number = data[0]
photos = data[1:]

ph_objects = []

for i in range(len(photos)):
    ph_objects.append(create_photo(i, photos[i]))

verticals = []
horizontals = []

for ph in ph_objects:
    if ph.orientation == "H":
        horizontals.append(ph)
    else:
        verticals.append(ph)

slides = [i for i in horizontals]

for i in range(0, len(verticals), 2):
    slides.append(Slide(verticals[i], verticals[i+1]))

random_results = []

for j in range(1):
    # random.shuffle(slides)
    slides = sorted(slides, key=lambda x: len(x.tags))

    final_score = 0

    for i in range(len(slides)-1):
        final_score += score(slides[i], slides[i+1])

    random_results.append(final_score)

print(max(random_results), min(random_results))

# res_file = open("outputs/e.txt", "a+")
# res_file.write(str(len(slides)) + "\n")
# for i in slides:
#     res_file.write(str(i.id) + "\n")
