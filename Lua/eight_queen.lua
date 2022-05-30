N = 8 --borad size
function ispalceok(a, n, c)
    for i = 1, n-1 do
        if (a[i] == c) or (a[i]-1 == c -n) or (a[i]+1 == c +n) then
            return false
        end
    end
    return true -- no attacks; place is ok!
end

-- print a board
function printsolution(a)  -- a是数组
    for i = 1, N do  --for each row
        for j = 1, N do  -- for each column
            io.write(a[i] == j and "x" or "-", " ")
        end
        io.write("\n")
    end
    io.write("\n")
end

-- add to board 'a' all queens from 'n' to 'N'
function addqueen(a, n)
    if n > N then
        printsolution(a)
    else
        for c = 1, N do
            if ispalceok(a, n, c) then
                a[n] = c
                addqueen(a, n+1)
            end
        end
    end
end

-- run
addqueen({}, 1)