# moby-credits-crashlands2
Converting Crashlands 2 credits JSON to mobygames text import format

# Requirements

- Python
- git-bash recommended, see https://github.com/FishieCat/Arma-Reforger-Credits-Extractor

# How to extract/convert

1. locate `GameData/gamechanger.json` and manually defile the JSON file so the credits 'groups' are the top level key:
  ![mutilatedjson](https://github.com/user-attachments/assets/1ac87700-7c19-49c5-85bf-83e092721bf7)
2. Save the mutilated file as `gamechanger.json` in a folder and save `moby_json_crashlands.py` from this repository there as well and run `python moby_json_crashlands.py gamechanger.json`
3. Manually check and correct stuff like `firstname "nickname" lastname` in `gamechanger.json_moby.txt`
