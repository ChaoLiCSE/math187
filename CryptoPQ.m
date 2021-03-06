function [ pt ] = CryptoPQ( P, Q, p )
    n = Q(1,1)-P(1,1)
    nInv = modInv(n, p)
    a = mod(nInv*(Q(1,2)-P(1,2)), p)
    x = mod(a^2-P(1,1)-Q(1,1), p)
    y = mod(-P(1,2)-a*(x-P(1,1)), p)
    pt = [x y]
end

