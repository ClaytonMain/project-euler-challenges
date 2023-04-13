import argparse
import os
import requests
import re
from markdownify import MarkdownConverter as MC
from bs4 import BeautifulSoup


def format_prompt_lines(soup: BeautifulSoup) -> str:
    converted = MC(sup_symbol='^').convert_soup(soup)
    # Fix images:
    converted = re.sub(
        r'(project/images/.*\.png)', r'https://projecteuler.net/\1', converted
    )
    # Fix superscript:
    converted = re.sub(r'\^(\d+)\^', r'<sup>\1</sup>', converted)
    prompt_lines = [f'> {x}' for x in converted.split('\n') if len(x)]
    return '\n>\n'.join(prompt_lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('n', type=int, help='The problem number')

    args = parser.parse_args()
    n = args.n

    padded_n = f'{n:04}'
    project_path = f'problems/problem{padded_n}/'
    if os.path.exists(project_path):
        print('\n*** Error! ***')
        print(
            f'Project path: "{project_path}" already exists!\n'
            'Please choose a different project number, or delete\n'
            'the existing project.'
        )
        raise SystemExit(1)

    os.makedirs(project_path)

    # I know it seems silly, but we're going to do two requests to get the
    # information needed for each problem. The problem_url request will
    # allow us to get the problem title and the difficulty rating. The
    # minimal_url request will allow us to get the problem description a
    # smidge easier (which should be handy for later problems that start
    # using LaTeX).
    problem_url = f'https://projecteuler.net/problem={n}'
    minimal_url = f'https://projecteuler.net/minimal={n}'

    s = requests.Session()
    r = s.get(problem_url)
    problem_soup = BeautifulSoup(r.text, 'html.parser')
    # Hoping that the first H2 element will always be the title, but will
    # update the code if that isn't the case in later problems.
    problem_title = problem_soup.find('h2').text
    tiptext = problem_soup.find('span', {'class': 'tooltiptext_right'}).text
    diff_rating = re.search(r'Difficulty rating: .*$', tiptext)[0]

    r = s.get(minimal_url)
    minimal_soup = BeautifulSoup(r.text, 'html.parser')

    with open(f'{project_path}README.md', 'x') as file:
        file.write(f'# [Problem {n} - {problem_title}]({problem_url})\n\n')
        file.write(f'{diff_rating}\n\n')
        file.write('## Prompt\n\n')
        prompt_lines = format_prompt_lines(minimal_soup)
        file.write(prompt_lines)

    with open(f'{project_path}problem_{padded_n}.py', 'x') as file:
        file.writelines(
            [
                f'# Project Euler: Problem {n} - {problem_title}\n',
                f'# {diff_rating}\n',
                'from helperfuncs.helper_funcs import time_decorator\n\n\n',
                '@time_decorator()\n',
                f'def p{padded_n}():\n',
                '    pass\n\n\n',
                'def main():\n',
                f'    ans = p{padded_n}()\n',
                "    print(f'\\n*** Answer ***\\n{ans}')\n\n\n",
                "if __name__ == '__main__':\n",
                '    main()\n\n',
                '# Output (SPOILERS)',
            ]
        )


if __name__ == '__main__':
    main()
