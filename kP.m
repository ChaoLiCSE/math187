function [ P ] = kP(k, P, A)
% Elliptic curve addition
%   kP = P + P + ... + P (k times)

    P
    k
    for iter = 1:k-1
        a = (3*P(1,1)^2 + A)/(2*P(1,2))
        x = a^2 - 2*P(1,1)
        y = -P(1,2)-a*(x-P(1,1)) 
        P = [x, y];
    end
end

