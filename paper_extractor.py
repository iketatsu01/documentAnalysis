import arxiv
from arxiv import SortCriterion, SortOrder
import pandas as pd

import csv

csv_path = 'paper.csv'

category = ['cs.AI', 'econ.EM', 'math.AC', 'astro-ph.CO', 'q-bio.BM']
n_cat = len(category)
n_paper_each_cat = 20

result_list = []

for i, cat in enumerate(category):
    arx = arxiv.Search(query='cat:'+cat+' AND submittedDate:[20230101 TO 20230515]',
                sort_by=SortCriterion.Relevance, sort_order=SortOrder.Descending, max_results=20)
    for j, result in enumerate(arx.results()):
        result_list.append([cat, result.summary])

with open(csv_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(result_list)
