import requests

base_url = 'https://projecteuler.net/minimal='

for problem_id in range(1, 714):
    try:
        url = base_url + str(problem_id)
        response = requests.get(url)
        response.raise_for_status()
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        with open('./problem_{}.md'.format(problem_id), 'w+') as f:
            f.write(response.text)
            f.close()

    with open('../README.md', 'a') as f:
        f.write(
            '[Problem {}](./problems/problem_{}.md)\n\n'.format(problem_id, problem_id))
