import argparse
import textwrap

def help_choise():
    parser = argparse.ArgumentParser(prog="connect_wired.py", formatter_class=argparse.RawDescriptionHelpFormatter, description=textwrap.dedent('''\
                Choise category and depth parse (pages)!
                ----------------------------------------
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
    parser.add_argument("number", type=int, help="Depth pase pages integer")
    parser.add_argument("category", help="Parse category https://www.wired.com/category/somewhat/")

    args = parser.parse_args()
    number = args.number
    category = args.category
    output_file = args.category + "_wired_titles"


    # if category == 'business':
    #     output_file = 'business_wired_titles'
    # elif category == 'culture':
    #     output_file = 'culture_wired_titles'
    # elif category == 'design':
    #     output_file = 'design_wired_titles'
    # elif category == 'gear':
    #     output_file = 'gear_wired_titles'
    # elif category == 'ideas':
    #     output_file = 'ideas_wired_titles'
    # elif category == 'science':
    #     output_file = 'science_wired_titles'
    # elif category == 'security':
    #     output_file = 'security_wired_titles'
    # elif category == 'transportation':
    #     output_file = 'transportation_wired_titles'
    # elif category == 'photo':
    #     output_file = 'photo_wired_titles'
    # elif category == 'video':
    #     output_file = 'video_wired_titles'
    # elif category == 'backchannel':
    #     output_file = 'backchannel_wired_titles'
    # elif category == 'video':
    #     output_file = 'video_wired_titles'
    # elif category == 'opinion':
    #     output_file = 'opinion_wired_titles'
    # elif category == 'magazine':
    #     output_file = 'magazine_wired_titles'



    return([number, category, output_file])

"""
For check function
"""    
# print(help_choise())