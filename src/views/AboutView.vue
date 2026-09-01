<script setup>
const board = [
  { role: 'Presidencia', name: 'Inmaculada Begoña Castro Pérez' },
  { role: 'Vicepresidencia', name: 'Roberto Rabina Simón' },
  { role: 'Secretaría', name: 'Pablo Rama Vilalta' },
  { role: 'Vicesecretaría', name: 'José Antonio Rama Patiño' },
  { role: 'Tesorería', name: 'Alberto Otero Vilariño' },
  { role: 'Contaduría', name: 'María Jesús Lourido Trillo' },
  { role: 'Primeiro vocal', name: 'Margarita Graña Bermúdez' },
  { role: 'Segundo vocal', name: 'Eloi Caamaño Lourido' },
  { role: 'Terceiro vocal', name: 'Guillermo Iglesias López' },
  { role: 'Cuarto vocal', name: 'José Antonio Vázquez Rivera' },
]
</script>

<template>
  <div class="container about">
    <h2 class="section-title">Sobre nós</h2>
    <hr class="divider" style="margin-left: 0" />

    <p>
      Semente Nova fundouse no 1981 coa idea de proporcionar á mocidade unha maneira de
      entretemento e unha formación pedagóxica e musical.
    </p>
    <p>
      A misión das seccións de danza é a de facer un traballo de investigación, de recollida de
      bailes, cancións, costumes e tradicións pola nosa autonomía, e nesta labor intentar
      divulgala.
    </p>
    <p>
      En canto á sección de rondalla e coral, os obxectivos e a idea básica é a de formar
      musicalmente á xuventude, así como crear un amplo arquivo musical para a difusión da
      música.
    </p>
    <p>
      Desde 1996, e co ánimo de ampliar os contactos con outras agrupacións e por tanto con
      outras tradicións, organizamos uns encontros folclóricos onde participaron formacións de
      distintas cidades de España e Portugal así como grupos de Centros Galegos en Suíza.
    </p>

    <h3 class="board-heading">Desde o 17 de febreiro de 2023 a directiva está formada por:</h3>
    <ul class="board-list">
      <li v-for="member in board" :key="member.role">
        <strong>{{ member.role }}:</strong> {{ member.name }}
      </li>
    </ul>
  </div>
</template>

<style scoped>
.about {
  padding-top: 24px;
  padding-bottom: 24px;
  max-width: 760px;
}

.about p {
  color: var(--color-text);
}

.board-heading {
  margin-top: 24px;
  margin-bottom: 10px;
  font-size: 15px;
  font-weight: 700;
  color: var(--color-heading);
}

.board-list {
  margin: 0;
  padding: 0;
  list-style: none;
}

.board-list li {
  padding: 5px 0;
  border-bottom: 1px solid var(--color-strip);
  font-size: 14px;
}

.board-list li:last-child {
  border-bottom: none;
}
</style>
