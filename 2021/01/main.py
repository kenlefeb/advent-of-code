
def process_line(line, previous):
    if previous is None:
        result = 'N/A - no previous measurement'

    else:
        result = 'increased' if line > previous else 'decreased'

    previous = line
    return result, previous

INPUT_FILE = 'input.txt'
OUTPUT_FILE = 'output.txt'
totals = {
    'increased': 0,
    'decreased': 0,
    'N/A - no previous measurement': 0
}

print(f'Beginning to process {INPUT_FILE} into {OUTPUT_FILE}')

with open(INPUT_FILE) as input:
    print(f'Opened {INPUT_FILE}')

    with open(OUTPUT_FILE, 'w') as output:
        print(f'Opened {OUTPUT_FILE} for writing')
        previous = None

        for line in input:
            line = line.strip()
            print(f'Processing line: {line}')
            result, previous = process_line(line, previous)
            output.write(f'{line} ({result})\n')
            totals[result] += 1

        print(f'Finished writing to {OUTPUT_FILE}')
        print(f'Totals: {totals}')
