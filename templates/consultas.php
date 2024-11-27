<?php
    include ("conexion.php");
    class Contacto extends Conexion{
        public function guardarDatosCalculadora($Calorias, $PesoAct, $Altura, $Genero, $PlanA){
            $this->sentencia = "DELETE FROM nutricion";
            $this->ejecutar_sentencia();
            $this->sentencia = "INSERT INTO nutricion VALUES (null, '$Calorias', '$PesoAct', '$Altura', '$Genero', '$PlanA')";
            $bandera=$this->ejecutar_sentencia();
        }

        public function consultarDatosCalculadora(){
            $this->sentencia = "SELECT * FROM nutricion";
            $resultado = $this->obtener_sentencia();
            return $resultado;
        }

        public function registrarPesoSemanal($fecha, $peso, $calorias_diarias){
            $this->sentencia = "INSERT INTO historial_peso VALUES (null, '$fecha', '$peso', '$calorias_diarias')";
            $this->ejecutar_sentencia();
        }

        public function consultarPesoSemanal(){
            $this->sentencia = "SELECT * FROM historial_peso";
            $resultado = $this->obtener_sentencia();
            return $resultado;
        }

        // Insertar un nuevo ejercicio en la rutina
        public function agregarEjercicio($dia, $noEjercicio, $ejercicio, $repeticiones, $peso) {
            $this->sentencia = "INSERT INTO rutina (Dia, NoEjercicio, Ejercicio, Repeticiones, Peso) 
                                VALUES ('$dia', '$noEjercicio', '$ejercicio', '$repeticiones', '$peso')";
            return $this->ejecutar_sentencia();
        }
        
        // Consultar todos los ejercicios de la rutina
        public function consultarRutina() {
            $this->sentencia = "SELECT * FROM rutina ORDER BY Dia, NoEjercicio";
            return $this->obtener_sentencia();
        }
        
        // Modificar un ejercicio específico
        public function modificarEjercicio($id, $noEjercicio, $ejercicio, $repeticiones, $peso) {
            $this->sentencia = "UPDATE rutina 
                                SET NoEjercicio = '$noEjercicio', Ejercicio = '$ejercicio', Repeticiones = '$repeticiones', Peso = '$peso' 
                                WHERE id = '$id'";
            return $this->ejecutar_sentencia();
        }
        
        // Eliminar un ejercicio de la rutina
        public function eliminarEjercicio($id) {
            $this->sentencia = "DELETE FROM rutina WHERE id = '$id'";
            return $this->ejecutar_sentencia();
        }
        
        // Consultar ejercicios de un día específico
        public function consultarPorDia($dia) {
            $this->sentencia = "SELECT * FROM rutina WHERE Dia = '$dia' ORDER BY NoEjercicio";
            return $this->obtener_sentencia();
        }
        
    }
?>
