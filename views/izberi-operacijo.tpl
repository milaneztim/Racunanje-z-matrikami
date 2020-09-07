<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta value="viewport" content="width=device-width, initial-scale=1.0">
	<title>Matrike</title>

	<style>

        .button {
            border: None;
            margin: 10px 10px;
        }

        table {
            border-collapse: collapse;
            width: 100%;
        }
	</style>
</head>
<body>	
	<h2>Izberite operacijo:</h2>
        <table>
            <form action="/vnos_matrike/B" method="POST" class="matrika">
                <tr>
                    <th><input type="image" src="/img/plus.png" alt="+" width="60" height="60" class="button" name="operacija" value="plus"></th>
                    <th><input type="image" src="/img/minus.png" alt="-" width="60" height="60" class="button" name="operacija" value="minus"></th>                
            </form>
            <form action="/vnos-dimenzije/B" method="POST" class="matrika">
                    <th><input type="image" src="/img/produkt.png" alt="*" width="60" height="60" class="button" name="operacija" value="produkt"></th>
            </form>
                </tr>    
                <tr>
            <form action="/vnos_matrike/B" method="POST" class="matrika">
                    <th><input type="image" src="/img/hadamard.png" alt="o" width="60" height="60" class="button" name="operacija" value="hadamard"></th>
                    <th><input type="image" src="/img/up-arrow.png" alt="^" width="60" height="60" class="button" name="operacija" value="potenca"></th> 
            </form>
            <form action="/rezultat/" method="POST" class="matrika">               
                    <th><input type="image" src="/img/det1.jpg" alt="det" width="110" height="70" class="button" name="operacija" value="det"></th>
                </tr>
                <tr>
                    <th><input type="image" src="/img/trace.jpg" alt="t" width="90" height="60" class="button" name="operacija" value="trace"></th>
                    <th><input type="image" src="/img/transpose.png" alt="tr" width="50" height="50" class="button" name="operacija" value="transpose"></th>            
                </tr>
            </form> 
	
</body>
</html> 