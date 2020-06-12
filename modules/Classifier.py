from fastai.vision import *
import pathlib

TYPES = [
    'alder tree',
    'ash tree',
    'beech tree',
    'birch tree',
    'cedar tree',
    'chestnut tree',
    'elm tree',
    'lime tree',
    'maple tree',
    'oak tree',
    'scots pine tree',
    'white poplar tree',
    'spruce tree',
    'willow tree'
]

DESCRIPTION = [
    "The common, or European, alder is part of the birch family and one of many alder species. It is a native British tree with dark grey bark, reddish twigs and dark green leaves. Alders can grow to 20 metres and live for up to 60 years. Their soft and porous wood lends itself to marine use. The alder is the only UK deciduous tree to produce cones.",
    "The native common ash is a deciduous tree (there are also evergreens among the many Ash species). It can grow to 35 metres high and live to over 400 years old. The ash has light browny-grey bark and light green compound leaves. The ash is particularly under threat from the Chalara Dieback fungal disease.",
    "The beech is a UK native deciduous tree. One of Britain’s largest trees, the beech can grow to 50 metres in height with a trunk diameter of over 3 metres, and live in some cases for over 300 years. The bark is smooth and grey, the leaves light green, getting ddarker with age. Beech wood is versatile and often used for burning.",
    "The birch is a deciduous hardwood with two types commonly found in the UK. The silver birch has white bark, pale green triangular leaves and can grow to around 30 metres high. The similar downy birch is so named because its leaves have downy stalks, unlike the hairless ones found on the silver birch.",
    "An evergreen conifer which can reach 35 metres in height, with spiral clusters of dark green needle-like leaves. Cedars are Lebanese or Eastern Mediterranean in origin and a favourite in the gardens of UK stately homes. They produce cones, usually every two years, which can be up to 12cm long.",
    "Chestnuts are deciduous trees which can reach 35 metres in height with a trunk up to 2 metres in diameter. Their leaves are pointed with pronounced veins. The two common types of chestnut tree are the sweet chestnut, which produce the eponymous edible fruit, and the conker-bearing horse chestnut.",
    "The elm is a native European deciduous tree with browny-grey bark and rounded, rough-haired leaves. Elms can live for over 100 years and grow up to 30 metres in height. There are numerous species, with the English Elm the most common in the UK. As the name suggests, Dutch Elm Disease is a particular threat to these trees.",
    "Three similar species can be found in the UK, small-leaved lime, large-leaved lime and common lime, a hybrid of the former two. Their bark is fissured and grey, their leaves asymmetrical with defined veins on the underside. The UK’s tallest broad-leaved tree, the common lime can grow to 50 metres in height.",
    "Similar to a sycamore, the field maple is a native deciduous tree with pale brown bark and small, dark green leaves which yellow in Autumn. Maple wood is particularly hard and dense which making it a favourite for making musical instruments.",
    "The English, or Common, Oak is the most common native British tree and a national icon. Oaks can grow to 40 metres in height and live to over 1000 years old. Its well-known fruit, the acorn, is a popular food with much of British wildlife. Its hard, dense wood has long been popular with architects and oak beams remain a favourite feature in the UK home.",
    "The Scots Pine is the only pine tree native to the UK. An evergreen conifer, a scots pine tree can reach 700 years old and grow 35 metres in height. These trees produce a particularly strong softwood, pine is widely used in the construction industry and for making the common telegraph pole.",
    "A deciduous broadleaf tree whose white twigs, pale bark and white-haired leaves can give it a snowy appearance. Of medium height (up to 20 metres), the poplar is a fast-growing tree and often used for screening or wind-break purposes.",
    "The Norway and Sitka Spruces are non-native to the UK but widely grown here for use as timber and the Norwegian in articular is a popular choice of Christmas Tree. These are evergreen conifers with straight trunks which can grow to 60 metres in height.",
    "Like the oak, the willow is a recognisable British emblem. There are numerous willow varieties in the UK including hybrids of the common species. The famous weeping willow, for example, is a hybrid of Chinese and European variants. The wood of the UK native white willow is used for making cricket bats."
]

def get_class(idx):
    return TYPES[idx]

def classify(img_path):
    path = pathlib.Path(__file__).parent.absolute()
    learn = load_learner(path, 'export.pkl')
    img = open_image(img_path)
    pred_class,pred_idx,outputs = learn.predict(img)
    return pred_class
