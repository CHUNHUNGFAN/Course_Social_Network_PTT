<template>
  <div id="app">
    <!-- <img src="./assets/logo.png">
    <h1>{{ msg }}</h1>
    <h2>Essential Links</h2>
    <ul>
      <li><a href="https://vuejs.org" target="_blank">Core Docs</a></li>
      <li><a href="https://forum.vuejs.org" target="_blank">Forum</a></li>
      <li><a href="https://chat.vuejs.org" target="_blank">Community Chat</a></li>
      <li><a href="https://twitter.com/vuejs" target="_blank">Twitter</a></li>
    </ul>
    <h2>Ecosystem</h2>
    <ul>
      <li><a href="http://router.vuejs.org/" target="_blank">vue-router</a></li>
      <li><a href="http://vuex.vuejs.org/" target="_blank">vuex</a></li>
      <li><a href="http://vue-loader.vuejs.org/" target="_blank">vue-loader</a></li>
      <li><a href="https://github.com/vuejs/awesome-vue" target="_blank">awesome-vue</a></li>
    </ul> -->

  <div>
    <full-page :options="options">
      <div class="section">
        <cover />
      </div>
      <div class="section">
        <div id="wrapper">
          <graph />
        </div>
      </div>
      <div class="section" >
        <div id="outer" style="width:1200px;">
          <div id="divl">
            <chart />
          </div>
          <div id="text-wrapper">
            <div id="text">Average Degree: 22.85</div>
            <div id="text">Average Clustering Coefficient: 0.71</div>
            <div id="text">Diameter: 4</div>
          </div>
        </div>
      </div>
      <div class="section" >
        <div id="outer2-wrapper">
          <div id="outer2" style="width:700px;">
            <chartDegreeCentrality />
          </div>
        </div>
      </div>
      <div class="section" >
        <div id="outer2-wrapper">
          <div id="outer2" style="width:700px;">
            <chartClosenessCentrality />
          </div>
        </div>
      </div>
    </full-page>
  </div>


  </div>
</template>

<script>
import cover from "./components/Cover.vue";
import graph from "./components/Graph.vue";
import chart from "./components/Chart.vue";
import chartDegreeCentrality from "./components/ChartDegreeCentrality.vue";
import chartClosenessCentrality from "./components/ChartClosenessCentrality.vue";

export default {
  name: 'app',
  components: {
    cover,
    graph,
    chart,
    chartDegreeCentrality,
    chartClosenessCentrality
  },
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}

#wrapper {
  margin: auto;
}

#outer {
  /* margin: 0 auto; */
  /* margin-left: auto;
  margin-right: auto; */
  margin: auto;
  display: flex;
  padding-left: 5px;
  padding-right: 5px;
}

#outer2-wrapper {
  /* text-align: center; */
  /* position: absolute; */
  display: flex;
}

#outer2 {
  /* margin-left: auto;
  margin-right: auto; */
  margin: auto;
}

#text-wrapper {
  display: table;
  width: 200px;
  padding-left: 0px;
}

#divl {
  width: 700px;
}

#text {
  width: 500px;
  margin-top: 60px;
  margin-left: 50px;
  text-align: left;
  font-size: 30px;
  font-family: 
}


</style>
