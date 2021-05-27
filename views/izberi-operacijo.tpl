<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta value="viewport" content="width=device-width, initial-scale=1.0">
	<title>Matrike</title>

	<style>

        .button {
            border: solid;
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
            <form action="/shrani-operacijo/" method="POST">
                <tr>
                    <th>
                        <button class="button" name="operacija" value="plus">
                            <img src="/img/plus.png" alt="+" width="60" height="60">
                        </button>
                    </th>
                    <th>
                        <button class="button" name="operacija" value="minus">
                            <img src="/img/minus.png" alt="-" width="60" height="60">
                        </button>
                    </th>                
                    <th>
                        <button class="button" name="operacija" value="produkt">
                            <img src="/img/produkt.png" alt="*" width="60" height="60">
                        </button>
                    </th>
                </tr>    
                <tr>
                    <th>
                        <button class="button" name="operacija" value="hadamard">
                            <img src="/img/hadamard.png" alt="o" width="60" height="60">
                        </button>
                    </th>
                    <th>
                        <button class="button" name="operacija" value="potenca">
                            <img src="/img/up-arrow.png" alt="^" width="60" height="60">
                        </button>
                    </th>             
                    <th>
                        <button class="button" name="operacija" value="det">
                            <img src="/img/det1.jpg" alt="det" width="100" height="70">
                        </button>
                    </th>
                </tr>
                <tr>
                    <th>
                        <button class="button" name="operacija" value="trace">
                            <img src="/img/trace.jpg" alt="tr" width="100" height="60">
                        </button>                        
                    </th>
                    <th>
                        <button class="button" name="operacija" value="transpose">
                            <img src="/img/transpose.png" alt="t" width="50" height="50">
                        </button>
                    </th>            
                </tr>
            </form> 
	
</body>
</html> 