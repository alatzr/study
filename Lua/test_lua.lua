days = {"��һ","�ܶ�","����","����","����","周六","周日"}
rev_days = {}
for k, v in pairs(days) do
    rev_days[v] = k
end

for k, v in pairs(rev_days) do
    print(k,":", v)
end