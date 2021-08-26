import argparse
import textwrap

def help_choise():
    parser = argparse.ArgumentParser(prog="game.py", formatter_class=argparse.RawDescriptionHelpFormatter, description=textwrap.dedent('''\
                Choise category and depth parse (pages)!
                --------------------------------
                    business
                    culture
                    design
                    gear
                    ideas
                    science
                    security
                    transportation
                    photo
                    video
                    backchannel
                    opinion
                    magazine
                    comcastbusiness

                For parse culture category on depth 100 pages type: parse_wired.py 100 culture
                '''))
    parser.add_argument("number", type=int, help="display a square of a given number")
    parser.add_argument("category", help="Parse category https://www.wired.com/category/somewhat/")

    args = parser.parse_args()
    number = args.number
    category = args.category
    return([number, category])

"""
For check function
"""    
# print(help_choise())