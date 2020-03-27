<script>
import { Bar } from 'vue-chartjs'

export default {
  extends: Bar,
  props: ['chartdata', 'options'],
  mounted () {
    this.renderChart({
      labels: ["0","1","3","5","6","7","8","9","10","11","12","13","14","15","16","17","18","20","21","22","23","25","26","27","28","29","30","31","32","33","34","35","37","39","41","42","43","44","47","49","51","53","60","68","70","71"],
      datasets: [
        {
          label: 'Degree Distribution',
          backgroundColor: '#ACD6FF',
          barThickness: 10,
          borderColor: '#ACD6FF',
          borderWidth: 1,
          data: [0,1,3,1,3,3,4,3,8,2,1,4,4,8,1,3,1,2,2,1,4,1,1,2,1,2,3,2,1,3,2,3,1,1,1,1,2,1,1,1,1,2,1,1,1,1]
        }
      ],
    })
  },
}
</script>

<style>
</style>
