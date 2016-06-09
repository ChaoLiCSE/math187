function [ P ] = CryptokP( k, P, A, p )
    for iter = 1:k-1
        n = 2 * P(1,2)
        nInv = modInv(n, p)
        a = mod(nInv * (3*P(1,1)^2 + A), p)
        x = mod(a^2 - 2*P(1,1), p)
        y = mod(-P(1,2) - a*(x - P(1,1)), p)
        P = [x y]
    end
end

