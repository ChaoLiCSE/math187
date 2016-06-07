function [ pt ] = PQ( P, Q )
% Elliptic Curve addition P+Q
    P
    Q
    a = (Q(1,2) - P(1,2)) / (Q(1,1) - P(1,1))
    x = a^2 - Q(1,1) - P(1,1)
    y = -P(1,2) - a*(x - P(1,1))
    
    pt = [x y];

end

