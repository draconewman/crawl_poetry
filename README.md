# crawl_poetry
First, I copied a portion of page_source from https://www.poetrystate.com/poetlist/ into a txt file which contains only poet links along with some unnecessary tags. 

save_all_links.py : removes those tags and extracts poet links, it is saved in a txt(poets_links.txt) file. 

poets_links.txt : contains all poets' links, total 600

sele.py : for this particular website, normal bs4 won't work, so i used selenium for web crawling. This is the main python program to extract poems from poet links, save those in a organised way in their individual poet folder.

to run this program type ->     python sele.py

there are total 2963 poems.
