import gpg

text = input("Write message")

c = gpg.core.Context(armor=True)