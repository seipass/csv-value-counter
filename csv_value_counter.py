import argparse,csv,json,sys
def transform(rows, column):
    from collections import Counter
    return dict(sorted(Counter(r.get(column,"") for r in rows).items()))

def main():
    parser=argparse.ArgumentParser(description='CSV value counter')
    parser.add_argument("file",nargs="?",help="input path; defaults to stdin")
    parser.add_argument("--column",required=True)
    args=parser.parse_args()
    source=open(args.file,encoding="utf-8",newline="").read() if args.file else sys.stdin.read()
    reader=csv.DictReader(source.splitlines())
    result=transform(list(reader))
    print(result if isinstance(result,str) else json.dumps(result,ensure_ascii=False,indent=2))

if __name__=="__main__": main()
