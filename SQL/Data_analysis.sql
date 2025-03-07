--1. Hər bir region üzrə ümumi satış məbləği.
--SELECT region, SUM(total_price) AS Total_Price From data_analysis GROUP BY region;
--2.Müxtəlif kateqoriyalar üzrə ümumi mənfəət.
--SELECT CATEGORY, SUM(profit) as "Total_Profit" FROM data_analysis GROUP BY CATEGORY;
--3.Müştəri adlarına görə ümumi alış miqdarı.
--SELECT customer_name,SUM(QUANTITY) AS TOTAL_QUANTIY FROM data_analysis GROUP BY customer_name; 
--4.Ödəniş üsulu üzrə ümumi endirim məbləği
--SELECT payment_method,SUM(DISCOUNT) AS "TOTAL_DISCOUNT" FROM data_analysis GROUP BY payment_method;
--5.Satış kanalına görə məhsul miqdarı.
--SELECT SALES_CHANNEL,SUM(QUANTITY) AS "TOTAL_QUANTITY" FROM data_analysis GROUP BY sales_channel; 
--6.Ən çox satış olan regionlar.
--SELECT REGION, SUM(QUANTITY) AS "TOTAL_QUANTITY" FROM data_analysis GROUP BY REGION ORDER BY TOTAL_QUANTITY DESC;
--7.Müxtəlif kateqoriyalar üzrə məhsul sayı və ümumi satış qiyməti.
--SELECT CATEGORY, SUM(QUANTITY) as "Total_Profit",SUM(TOTAL_PRICE) AS TOTAL_PRICE FROM data_analysis GROUP BY CATEGORY;
--8.2023-cü ildə edilən satışların ümumi mənfəəti.
--SELECT SUM(PROFIT) AS "TOTAL_PROFIT" FROM data_analysis WHERE EXTRACT(YEAR FROM SALE_DATE)=2023;
--9.Müxtəlif regionlarda hansı ödəniş üsulunun daha çox istifadə edildiyinin hesablanmasi.
--SELECT REGION,PAYMENT_METHOD, COUNT(PAYMENT_METHOD) AS PAYMENT_COUNT FROM data_analysis GROUP BY region,Payment_method ORDER BY region,PAYMENT_COUNT DESC;
--10.Satış kanalı və ödəniş üsulu üzrə ümumi mənfəət.
--SELECT SALES_CHANNEL,PAYMENT_METHOD,SUM(PROFIT) FROM data_analysis GROUP BY sales_channel,Payment_method;
--11.Hər bir region üzrə məhsul qaytarılma faizi.
--SELECT region, (COUNT(CASE WHEN return_status = 'Returned' THEN 1 END) * 100.0) / COUNT(*) AS return_percentage FROM data_analysis GROUP BY region;
--12.Məhsul kateqoriyalarına görə ən çox mənfəət gətirən məhsullar.
--SELECT PRODUCT_NAME,SUM(PROFIT) AS TOTAL_PROFIT FROM data_analysis GROUP BY PRODUCT_NAME ORDER BY TOTAL_PROFIT DESC FETCH FIRST 5 ROW ONLY;
--13.Endirimli məhsullar ümumi gəlirin neçə faizini əldə etmetinin hesablanmasi
--SELECT (SUM(CASE WHEN DISCOUNT > 0 THEN TOTAL_PRICE ELSE 0 END) / SUM(TOTAL_PRICE)) * 100 AS PRODUCTS_PERCENTAGE FROM data_analysis;
--14.Ən çox satış gəliri  əldə edilən il 
--SELECT TO_CHAR(sale_date, 'YYYY') AS SALE_YEAR, SUM(PROFIT) AS TOTAL_PROFIT FROM data_analysis GROUP BY TO_CHAR(sale_date, 'YYYY') ORDER BY TOTAL_PROFIT DESC FETCH FIRST 1 ROW ONLY;
--15.Ən çox alış-veriş edən  müştəri 
--SELECT CUSTOMER_NAME,SUM(QUANTITY) AS TOTAL_QUANTITY FROM data_analysis GROUP BY CUSTOMER_NAME FETCH FIRST 1 ROW ONLY;
--16.Hər bir məhsul kateqoriyasına görə geri qaytarılmış məhsul sayı   
--SELECT CATEGORY, (COUNT(CASE WHEN return_status='Returned' THEN 1 END)) as COUNT_PRODUCT FROM data_analysis GROUP BY category;
--17.Regionlara görə endirimlər hansı kateqoriyalarda daha çox tətbiq edilməsinin hesablanması
--SELECT  REGION , CATEGORY, SUM(DISCOUNT) AS TOTAL_DISCOUNT  FROM data_analysis GROUP BY REGION,CATEGORY ORDER BY TOTAL_DISCOUNT DESC FETCH FIRST 5 ROW ONLY
--18.Hər bir kateqoriyada tətbiq olunan orta endirim məbləği.
--SELECT CATEGORY, AVG(DISCOUNT) AS AVARAGE_DISCOUNT FROM data_analysis GROUP BY category;
--19.Həftənin hansı günləri ən çox satış edilməsinin hesablanması
--SELECT TO_CHAR(SALE_DATE,'Day') AS SALE_DAY,  COUNT(*) AS TOTAL_SALES FROM data_analysis GROUP BY TO_CHAR(SALE_DATE,'Day') ORDER BY TOTAL_SALES DESC;
--20.Ən çox məhsul satılan ay 
--SELECT TO_CHAR(SALE_DATE,'Month') AS SALE_MONTH, SUM(QUANTITY) AS TOTAL_QUANTITY FROM data_analysis GROUP BY TO_CHAR(SALE_DATE,'Month') ORDER BY TOTAL_QUANTITY DESC;


