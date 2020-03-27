<template>
  <div class="act-form">
    <iframe :src="src" width="1280" height="640" scrolling="no" frameBorder="0"></iframe>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        src: 'http://140.120.13.177:8080/public/index.html'
      }
    },
    mounted () {
      console.log(this.$refs.iframe)
  }
}
</script>

<style>
</style>
