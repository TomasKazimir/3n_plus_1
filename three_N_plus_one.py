from itertools import islice


def main(n: int):
    if n <= 1:
        return {n: 0}
    x = int(n)
    output = str(n)
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        output += f' => {n}'
    return {x: len(output.split(' => ')) - 1}


if __name__ == '__main__':
    a = {}
    for x in range(1000):
        a.update(main(x))
    for key, value in islice(dict(sorted(dict(sorted(a.items(), key=lambda x: x[1], reverse=True)).items(), key=lambda x: x[1], reverse=True)).items(), 100):
        print(f'{key} - {value}')
