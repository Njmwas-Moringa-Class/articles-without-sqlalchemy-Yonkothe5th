#!/usr/bin/env python3
import sys
sys.path.append('lib')

import ipdb;


from Author import Author
from Magazine import Magazine
from Article import Article

if __name__ == '__main__':
#  WRITE YOUR TEST CODE HERE ###
    author1 = Author("Jekyl D Law")
    author2 = Author("Clyde Ombachi")
    
    ipdb.set_trace()
    
    magazine1 = Magazine("New York Times", "Cosmopolitan")
    magazine2 = Magazine("Almanac of the year", "Glam mag")

    # Insert a breakpoint here to interact with the terminal
    ipdb.set_trace()

    article1 = author1.add_article(magazine1, "The sharp decline of the dollar")
    article2 = author2.add_article(magazine1, "Ten ways to kepp a healthy skin")
    article3 = author1.add_article(magazine2, "Deep sea treasures")

    # Test code
    print("Authors:")
    for author in Author.all():
        print(author.name())

    print("\nMagazines:")
    for magazine in Magazine.all():
        print(f"{magazine.name()} - {magazine.category()}")

    print("\nArticles:")
    for article in Article.all():
        print(f"{article.title()} by {article.author().name()} in {article.magazine().name()}")
# DO NOT REMOVE THIS
    ipdb.set_trace()
