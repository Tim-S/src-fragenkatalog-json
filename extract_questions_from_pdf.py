import argparse
import json
import re
import urllib.parse
import urllib.request
import camelot.io as camelot

def main():
  parser = argparse.ArgumentParser(
                    description='Parse Questions from PDF-Tales and ouput in json form (for quiz)',
                    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument('--url', default="", help="URL")
  parser.add_argument('--pdf', default="Fragenkatalog-SRC-2018.pdf", help="PDF File")
  parser.add_argument('--pages', default="3-end", help="specify PDF Pages")
  parser.add_argument('--json', default="questions.json", help="ouput-path of json-file")

  args = parser.parse_args()

  path_pdf_file = args.pdf
  path_json = args.json 

  if(args.url):
    url = args.url
    urllib.parse.urlparse(url).scheme in ('http', 'https', 'ftp')
    print(f"Downloading {url} to {path_pdf_file}...")
    urllib.request.urlretrieve(url, path_pdf_file)
    print(f"Downloaded {url} to {path_pdf_file}")

  print(f"Extract Data from {path_pdf_file} (this may take a while)...")
  tables = camelot.read_pdf(path_pdf_file, pages=args.pages)

  _re = re.compile(r"^(\w)\s+")
  
  def fix_text_single_starting_letter(text: str):
    return _re.sub(lambda match : '' if match.group(1) is None else match.group(1), text)

  print(f"Creating JSON-representation of Questions in {path_json}")
  data = {}
  data = {"questions": []}

  for table in tables:
      q = {}

      df = table.df
      it = df.iterrows()
      i, first_row = next(it)
      txt_question = first_row[1]
      txt_question = fix_text_single_starting_letter(txt_question)
      
      q["question"] = txt_question
      choices = []

      for i, row in it:
        txt_answer_option = row[1]
        txt_answer_option = fix_text_single_starting_letter(txt_answer_option)
        choices.append(txt_answer_option)
      q["choices"] = choices
      q["correctAnswer"] = choices[0] # NOTE: "Richtig ist immer die Antwort 1."
      data["questions"].append(q)

  json_data = json.dumps(data, indent=2)
  with open(path_json, "w") as outfile:
    outfile.write(json_data)

if __name__ == '__main__':
  main()
