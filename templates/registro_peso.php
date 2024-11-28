<!DOCTYPE html>
<html>
<head>
    <title>Registro de Peso</title>
</head>
<style>
  body {
    font-family: Arial, sans-serif;
    margin: 20px;
    background-color: #f2f2f2;
  }
  
  h1, h2 {
    text-align: center;
    color: #333;
  }
  
  .container {
    max-width: 600px;
    margin: 0 auto;
    padding: 20px;
    background-color: white;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  }
  
  form {
    margin-bottom: 20px;
  }
  
  input[type="number"] {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  input[type="submit"] {
    background-color: #4CAF50;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  input[type="submit"]:hover {
    background-color: #45a049;
  }
  
  table {
    width: 100%;
    border-collapse: collapse;
  }
  
  th, td {
    padding: 10px;
    text-align: left;
    border-bottom: 1px solid #ddd;
  }
  
  th {
    background-color: #f2f2f2;
  }
  
  a.home-link {
    display: block;
    text-align: center;
    color: #4CAF50;
    text-decoration: none;
    margin-top: 20px;
  }
  
  a.home-link:hover {
    color: #45a049;
  }  
  li {
    margin-bottom: 10px;
  }
  
  a {
    text-decoration: none;
    color: #4CAF50;
    font-size: 18px;
  }
  
  a:hover {
    color: #45a049;
  }
  </style>
<body>
    <h1>Registro de Peso</h1>
    <form method="POST">
        <label>Peso (kg): <input type="number" name="peso" step="0.1" required></label><br>
        <label>Calorias Diarias (cal): <input type="number" name="calorias" step="0.1" required></label><br>
        <input type="submit" value="Registrar">
    </form>

    <h2>Historial de Peso</h2>
    <table border="1">
        <tr>
            <th>Fecha</th>
            <th>Peso</th>
            <th>Calorias Diarias</th>
        </tr>
        {% for registro in historial %}
        <tr>
            <td>{{ registro.Fecha }}</td>
            <td>{{ registro.Peso }}</td>
            <td>{{ registro.calorias_diarias }}</td>
        </tr>
        {% endfor %}
    </table>

    <br>
    <li><a href="{{ url_for('index') }}">Volver al Inicio</a></li>
</body>
</html>

<?php
  if(isset($_POST['Registrar']))
  {
    $fecha = date("Y/m/d");
    $peso = $_POST['peso'];
    $cals = $_POST['calorias'];
    require_once('consultas.php');
    $obj = new Contacto();
    $obj->registrarPesoSemanal($fecha,$peso,$cals);
    echo "si";
  }
  ?>