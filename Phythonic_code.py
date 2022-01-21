# split
# java의 StringTokenizer에서 자동으로 list 저장까지 해주는 함수

items = 'zero one two three'
items.split()

print(items)

langs = 'python,jquery,javascript,pascal'
a,b,c,d = langs.split(",")

print(d)

example = "cs50.gachon.edu"
subdomain, domain, tld = example.split(".")
print(domain)

#join

