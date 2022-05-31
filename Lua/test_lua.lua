days = {"周一","周二","周三","周四","周五","鍛ㄥ叚","鍛ㄦ棩"}
rev_days = {}
for k, v in pairs(days) do
    rev_days[v] = k
end

for k, v in pairs(rev_days) do
    print(k,":", v)
end