from nose.tools import *
from anime_renamer import *


def test_meta_data_extraction():
  naruto_example = "[HorribleSubs]_Naruto_Shippuuden_-_296_[720p].mkv"
  naruto_expectation = {'anime': "Naruto_Shippuuden",
                        'episode': "296",
                        'extension': "mkv"}
  eq_(naruto_expectation,
      extract_meta_data(naruto_example))

  bebop_example = "/home/xbmc/Media/Animes/OZC Cowboy Bebop Remastered E20 Pierrot Le Fou/[OZC]Cowboy_Bebop_Remastered_E20_'Pierrot_Le_Fou'.mkv"
  bebob_expectation = {'anime': "Cowboy_Bebop",
                        'episode': "20",
                        'extension': "mkv"}
