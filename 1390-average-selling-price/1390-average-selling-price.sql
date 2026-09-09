SELECT 
    p.product_id,
    ROUND(IFNULL(SUM(p.price * ut.units) / SUM(ut.units), 0), 2) AS average_price
FROM 
    Prices p  
LEFT JOIN 
    UnitsSold ut 
ON 
    p.product_id = ut.product_id 
    AND ut.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY 
    p.product_id;
