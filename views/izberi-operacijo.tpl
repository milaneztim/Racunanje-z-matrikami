<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta value="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.css">
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
                            <img src="/img/plus.png" alt="+" width="120" height="120">
                        </button>
                    </th>
                    <th>
                        <button class="button" name="operacija" value="minus">
                            <img src="/img/minus.png" alt="-" width="120" height="120">
                        </button>
                    </th>                
                    <th>
                        <button class="button" name="operacija" value="produkt">
                            <img src="/img/produkt.png" alt="*" width="120" height="120">
                        </button>
                    </th>
                </tr>    
                <tr>
                    <th>
                        <button class="button" name="operacija" value="hadamard">
                            <img src="/img/hadamard.png" alt="o" width="120" height="120">
                        </button>
                    </th>
                    <th>
                        <button class="button" name="operacija" value="potenca">
                            <img src="/img/up-arrow.png" alt="^" width="120" height="120">
                        </button>
                    </th>             
                    <th>
                        <button class="button" name="operacija" value="transpose">
                            <img src="/img/transpose.png" alt="t" width="120" height="120">
                        </button>
                    </th>
                </tr>
                <tr>
                    <th>
                        <button class="button" name="operacija" value="trace">
                            <img src="/img/trace.jpg" alt="tr" width="150" height="90">
                        </button>
                    </th>
                    <th>
                        <button class="button" name="operacija" value="det">
                            <img src="/img/det.jpg" alt="det" width="150" height="95">
                        </button>
                    </th>          
                </tr>
            </form> 
	
</body>
</html> 