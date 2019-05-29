local t={}

table.insert(t,1)
table.insert(t,2)
table.insert(t,3)

table.sort(t,function(a,b)
	return a>b
end)

print(t[1])