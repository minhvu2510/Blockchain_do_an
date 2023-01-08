<template>
  <div style="margin-top: -60px;width: 100%">
    <!--<el-header>Header</el-header>-->
    <el-container style="height: 800px">
      <el-aside width="350px" style="background-color: rgb(238, 241, 246); height: 800px">
        <el-header style=" background-color: white; text-align: left">

          <img src="http://qldt.ptit.edu.vn/MessageFile/242794Logo2.gif" alt="Italian Trulli" width="60" height="60" style="text-align: left">
          <img src="data:image/jpeg;base64,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" alt="Italian Trulli" width="160" height="60" style="margin-left: 25px">
        </el-header>
        <el-menu :default-openeds="['1', '3']">
          <el-row>
            <!--<span>1/12</span>-->
            <el-progress :percentage="percen_ans" :format="format"></el-progress>
          </el-row>
          <!--<h3>Trả lời</h3>-->
          <el-table
                  row-click=myFuntion(757)
                  :data="table_answer"
                  header-align="center"
                  style="width: 100%">
            <el-table-column
                    align="center"
                    prop="index"
                    label="Câu hỏi">
            </el-table-column>
            <el-table-column
                    label="Xóa câu trả lời">
              <template slot-scope="scope">
                <!--<div>-->
                  <!--<el-link type="danger">{{scope.row.ans}}</el-link>-->
                  <!--&lt;!&ndash;<el-button @click="myFuntion(scope.row.ind)" type="danger" icon="el-icon-delete" plain size="mini">Xóa</el-button>&ndash;&gt;-->
                  <!--&lt;!&ndash;<audio controls>&ndash;&gt;-->
                  <!--&lt;!&ndash;<source :src="scope.row.url_storage" type="audio/ogg">&ndash;&gt;-->
                  <!--&lt;!&ndash;<source :src="scope.row.url_storage" type="audio/mpeg">&ndash;&gt;-->
                  <!--&lt;!&ndash;Your browser does not support the audio element.&ndash;&gt;-->
                  <!--&lt;!&ndash;</audio>&ndash;&gt;-->
                <!--</div>-->
                <div v-if="scope.row.ans === 'Chưa trả lời'">
                  <el-link @click="myFuntion(scope.row.idi)" type="danger">{{scope.row.ans}}</el-link>
                </div>
                <div v-else>
                  <el-link @click="myFuntion(scope.row.idi)" type="success">{{scope.row.ans}}</el-link>
                </div>
                <!--<div>-->
                <!--<el-button :disabled="check" @click="delete_ans(scope.$index)" type="danger" icon="el-icon-delete" plain size="mini">Xóa</el-button>-->
                <!--</div>-->
              </template>
            </el-table-column>
            <!--<el-table-column-->
                    <!--align="center"-->
                    <!--prop="ans"-->
                    <!--label="Câu trả lời">-->
            <!--</el-table-column>-->
            <el-table-column
                    label="Xóa câu trả lời">
              <template slot-scope="scope">
                <div>
                  <el-button @click="delete_ans(scope.$index)" type="danger" icon="el-icon-delete" plain size="mini">Xóa</el-button>
                </div>
              </template>
            </el-table-column>
          </el-table>
          <div style="padding-top: 10px;padding-bottom: 10px">
            <small style="color: #3A71A8">Hệ thống sẽ tự động nộp bài khi hết thời gian</small>
          </div>
          <div style="padding-top: 10px;padding-bottom: 10px">
            <el-button type="primary" @click="nopbai" plain>Nộp bài</el-button>
          </div>

          <!--<div style="padding-top: 15px">-->
            <!--<el-progress type="circle" :percentage="100" status="success"></el-progress>-->
          <!--</div>-->
        </el-menu>
      </el-aside>

      <el-container>
        <!--<el-header>-->
          <!--<el-progress :percentage="100" status="success"></el-progress>-->
        <!--</el-header>-->
        <el-header>
         <el-row>
           <el-col :span="20">
             <div style="color: #3A71A8; font-size: 30px; font-weight: bold">BÀI  THI TRẮC NHIỆM MÔN  TIẾNG  ANH</div>
             <!--<small>Thời gian làm bài 45'</small>-->
           </el-col>
           <!--<el-progress style="width: 100%" :percentage="100" status="success"></el-progress>-->
           <el-col :span="4">
             <div style="text-align: right">
               <el-dropdown style="top: 5%">
                 <!--<i class="el-icon-user-solid" style="margin-right: 15px"></i>-->
                 <el-avatar :size="50" src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"></el-avatar>
                 <el-dropdown-menu slot="dropdown">
                   <el-dropdown-item>View</el-dropdown-item>
                   <el-dropdown-item>Add</el-dropdown-item>
                   <el-dropdown-item>Delete</el-dropdown-item>
                 </el-dropdown-menu>
               </el-dropdown>
               <span>Minh Vũ</span>
             </div>
           </el-col>
         </el-row>
          <!--<el-progress style="width: 100%" :percentage="100" status="success"></el-progress>-->
          <!--<el-tag type="success">minhvu</el-tag>-->
          <div>
            <!--<el-tag type="success"><p style="font-size: 20px">{{ minutes }}:{{ seconds }}</p></el-tag>-->
          </div>
        </el-header>
        <div style="padding-left: 13px">
          <el-row>
            <el-col :span="2">
              <el-tag type="success" style="font-size: 18px;height: 30px">
                <div style="padding-top: 2px">
                  {{ minutes }}:{{ seconds }}
                </div>
              </el-tag>
            </el-col>
            <el-col :span="22">
              <el-progress style="width: 100%" :percentage="percent" :status=status ></el-progress>
            </el-col>
          </el-row>
          <!--<el-progress style="width: 100%" :percentage="seconds" status="success"></el-progress>-->
        </div>

        <el-main>
          <!--<el-progress :percentage="100" status="success"></el-progress>-->
          <!--<el-card class="box-card" shadow="hover">-->
            <!--<div slot="header" class="clearfix" style="text-align: left">-->
              <!--<span>Card name</span>-->
              <!--<el-button style="float: right; padding: 3px 0" type="text">Operation button</el-button>-->
            <!--</div>-->
            <!--<div style="text-align: left">-->
              <!--<p>Fast & Furious 6 ................... at number one at the North American box office, taking more than double The Hangover Part III's opening takings.</p>-->
              <!--<el-row>-->
                <!--<el-col :span="2"><br/></el-col>-->
                <!--<el-col :span="10">-->
                  <!--<el-radio :label="3"><b><big>A : </big></b> will debute</el-radio>-->
                <!--</el-col>-->
                <!--<el-col :span="10">-->
                  <!--<el-radio :label="3"><b><big>B : </big></b> will debute</el-radio>-->
                <!--</el-col>-->
              <!--</el-row>-->
              <!--<el-row style="padding-top: 10px; margin-top: 10px">-->
                <!--<el-col :span="2"><br/></el-col>-->
                <!--<el-col :span="10">-->
                  <!--<el-radio :label="3"><b><big>C : </big></b> will debute</el-radio>-->
                <!--</el-col>-->
                <!--<el-col :span="10">-->
                  <!--<el-radio :label="3"><b><big>D : </big></b> will debute</el-radio>-->
                <!--</el-col>-->
              <!--</el-row>-->
            <!--</div>-->
            <!--&lt;!&ndash;<div v-for="o in 4" :key="o" class="text item">&ndash;&gt;-->
              <!--&lt;!&ndash;{{'List item ' + o }}&ndash;&gt;-->
            <!--&lt;!&ndash;</div>&ndash;&gt;-->
          <!--</el-card>-->
          <!--<br/>-->
          <!--<div>{{this.table_answer}}</div>-->
          <div style="margin-top: -17px">
            <div v-for="(item, index) in questions" :key="index" style="padding-top: 10px">
              <!--<el-steps :space="50" :active="1" simple>-->
              <!--<el-step style="margin-left: -35px" :title= "'Câu ' + (parseInt(index) + 1) + ':'" icon="el-icon-edit"></el-step>-->
              <!--</el-steps>-->
              <div :id=item.idi class="header1">
                <h3 class="vertical-center">Câu {{index + 1}}:</h3>
              </div>
              <!--<h3 style="text-align: left;padding-left: 30px">Câu {{index + 1}}:</h3>-->
              <p style="text-align: left;padding-left: 30px">{{item.question}}</p>
              <el-row style="padding-left: 30px; padding-top: 10px">
                <!--<el-col :span="1"><br/></el-col>-->
                <el-col :span="2" @click="test_click">
                  <!--<el-radio @click="test_click" v-model=table_answer[index].ans label="A"><b><big>A : </big></b> {{item.answer[0]}}</el-radio>-->
                  <el-radio v-model=check :label="'A|' + item.idi + '|' + item.answer[0]"><b><big>A : </big></b> {{item.answer[0]}}</el-radio>
                </el-col>
                <el-col :span="8"><br/></el-col>
                <el-col :span="6">
                  <!--<el-radio v-model=table_answer[index].ans label="B"><b><big>B : </big></b> {{item.answer[1]}}</el-radio>-->
                  <el-radio v-model=check :label="'B|' + item.idi + '|' + item.answer[1]"><b><big>B : </big></b> {{item.answer[1]}}</el-radio>
                </el-col>
              </el-row>
              <!--<el-radio v-model="radio" label="1">Option A</el-radio>-->
              <!--<el-radio v-model="radio" label="2">Option B</el-radio>-->
              <!--<el-radio v-model="radio" label="3">Option C</el-radio>-->
              <el-row style="padding-top: 15px; margin-top: 15px;padding-left: 30px">
                <!--<el-col :span="1"><br/></el-col>-->
                <el-col :span="2">
                  <!--<el-radio v-model=table_answer[index].ans label="C"><b><big>C : </big></b> {{item.answer[2]}}</el-radio>-->
                  <el-radio v-model=check :label="'C|' + item.idi  + '|' + item.answer[2]"><b><big>C : </big></b> {{item.answer[2]}}</el-radio>
                </el-col>
                <el-col :span="8"><br/></el-col>
                <el-col :span="6">
                  <!--<el-radio v-model=table_answer[index].ans label="D"><b><big>D : </big></b> {{item.answer[3]}}</el-radio>-->
                  <el-radio v-model=check :label="'D|' + item.idi + '|' + item.answer[3]"><b><big>D : </big></b> {{item.answer[3]}}</el-radio>
                </el-col>
              </el-row>
            </div>
          </div>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
  import { get_question } from '@/api/questions'
  import { answers } from '@/api/questions'
export default {
  name: 'HelloWorld',
  data() {
    const item = {
      date: '2016-05-02',
      name: 'Tom',
      address: 'No. 189, Grove St, Los Angeles'
    };
    return {
      tableData: Array(20).fill(item),
      status: 'success',
      questions: [],
      totalTime: (4 * 60),
      percent: 0,
      table_answer: [],
      radio: '',
      check: '',
      percen_ans: 0
    }
  },
  mounted() {
    this.all_questions()
    if (this.totalTime === (4 * 60)) {
      this.startTimer()
    }
    // // this.name = this.$route.params.id_certificate
    // if(this.$store.getters.role === 'admin') {
    //   this.get_certificate_detail()
    //   this.all_user()
    // } else {
    //   // var k = {label: this.$store.getters.email, value: this.$store.getters.id}
    //   // this.options_account = [{label: this.$store.getters.email, value: this.$store.getters.id}]
    //   // this.list_acc = [this.$store.getters.id]
    //   this.disble_member = true
    //   this.get_certificate_detail()
    // }
  },
  methods: {
    myFuntion (id){
      console.log(id)
      var elmnt = document.getElementById(id);
      elmnt.scrollIntoView();
    },
    send_answers() {
      var arr = ''
      for (const i in this.table_answer) {
        // var k = {'idi': this.table_answer[i].idi, 'result': this.table_answer[i].result}
        var k = this.table_answer[i].idi.toString() + '|' + this.table_answer[i].result
        if(arr === '') {
          arr = arr + k
        }else {
          arr = arr + '-' + k
        }
      }
      const data = {
        account_id: 'vudeptrai',
        list_ans: arr
      }
      // var id = this.$route.params.id_certificate
      // console.log('id', id)
      answers(data).then(res => {
        console.log(res)
        this.$notify({
          title: 'Thành công',
          message: res.message,
          type: 'success'
        })
      }, respone => {
        console.log(respone)
        this.$notify({
          title: 'Lỗi (error)',
          message: respone.message,
          type: 'info'
        })
        // this.notify('info', respone.body.message)
      })
    },
    all_questions() {
      // const param = {page: 1, limit: 100}
      get_question()
              .then(res => {
                console.log(res.data.status)
                if(res.data.status === 'ok') {
                  var dem = 0;
                  this.questions = res.data.data
                  for( var i in this.questions) {
                    dem += 1;
                    // console.log(res.data.data[i])
                    this.questions[i]['selec'] = 'Chưa trả lời'
                    this.questions[i]['index'] = dem
                    var data = {'idi': this.questions[i].idi, 'ans': 'Chưa trả lời', 'index': dem, 'result': ''}
                    this.table_answer.push(data)
                    // this.questions.push("dm")
                  }

                }
                console.log(this.questions)
                // console.log(res)
                // var arr_acc = res.data.results
                // for (var i in arr_acc) {
                //   if(this.$store.getters.email !== arr_acc[i].email) {
                //     var k = {label: arr_acc[i].email, value: arr_acc[i].id}
                //     this.options_account.push(k)
                //   }
                //
                // }
              })
    },
    test_click() {
      // console.log('00000000000000000000000000000000000')
    },
    format(int_ans) {
      console.log(int_ans)
      console.log(typeof (int_ans))
      var dm = int_ans / 100 * 12
      var ts = Math.ceil(dm)
      var k = ts.toString() + '/12'
      return k;
    },
    delete_ans(data) {
      // console.log(this.table_answer['ans'])
      // console.log(this.table_answer['ans'])
      this.table_answer[data]['ans'] = 'Chưa trả lời'
      this.table_answer[data].result = 'Chưa trả lời'
    },

    // set_answer() {
    //
    // },
    startTimer: function() {
      this.timer = setInterval(() => this.countdown(), 1000)
      this.resetButton = true
      this.edit = false
    },
    stopTimer: function() {
      clearInterval(this.timer)
      this.timer = null
      this.resetButton = true
    },
    resetTimer: function() {
      this.totalTime = (this.userTime * 60)
      clearInterval(this.timer)
      this.timer = null
      this.resetButton = false
    },
    editTimer: function() {
      this.edit = !this.edit
    },
    padTime: function(time) {
      return (time < 10 ? '0' : '') + time
    },
    countdown: function() {
      this.totalTime--
    },
    get_percent() {
      var minu = parseInt(this.minutes) * 60 + parseInt(this.seconds)
      this.percent = parseInt(minu / (4 * 60) * 100)
    },
    nopbai() {
      var dem = 0
      for (const ans in this.table_answer){
        if(this.table_answer[ans].ans != "Chưa trả lời"){
          dem += 1
        }
      }
      var noti = ''
      if ( dem === 12){
        noti = "Xác nhận nộp bài"
      } else {
        var cl = 12 - dem
        noti = "Bạn còn " + cl.toString() + " câu chưa trả lời. Bạn vẫn muốn nộp bài"
      }
      this.$confirm(noti, 'Xác nhận', {
        dangerouslyUseHTMLString: true,
        confirmButtonText: 'Nộp bài',
        cancelButtonText: 'Thoát',
        type: 'warning'
      }).then(() => {
        this.send_answers()
        // this.$message({
        //   type: 'success',
        //   message: 'Delete completed'
        // })
      }).catch(() => {
      })
    }
  },
  computed: {
    minutes: function() {
      const minutes = Math.floor(this.totalTime / 60)
      return this.padTime(minutes)
    },
    seconds: function() {
      const seconds = this.totalTime - (this.minutes * 60)
      return this.padTime(seconds)
    }
  },
  watch: {
    'seconds'() {
      // console.log(this.minutes)
      // console.log(typeof (this.minutes))
      if (this.minutes === '01') {
        this.status = 'exception'
      }
      if (this.minutes === '02') {
        this.status = 'warning'
      }
      if (this.minutes === '00' && this.seconds === '00') {
        this.stopTimer()
      }
      // console.log('vudeptrai')
      this.get_percent()
    },
    'questions'() {
      console.log(this.questions)
    },
    'table_answer'() {
      console.log('vlvlvlvlvlvl')
    },
    'check'() {
      // console.log(this.check)
      var da = this.check.split("|")[0]
      var id = Number(this.check.split("|")[1])
      var re = (this.check.split("|")[2])
      // console.log(da)
      // console.log(id)
      // console.log(typeof (id))
      for (const ans in this.table_answer){
        console.log(typeof (this.table_answer[ans].idi))
        if(this.table_answer[ans].idi === id){
          console.log('dmdmdm111')
          this.table_answer[ans].ans = da
          this.table_answer[ans].result = re
        }
      }
      var dem = 0
      for (const ans in this.table_answer){
        if(this.table_answer[ans].ans != "Chưa trả lời"){
          dem += 1
        }
      }
      this.percen_ans = dem/12 * 100
      // this.format(7)
    }
  }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .el-header {
    /*position: absolute;*/
    /*top: 50%;*/
    /*background-color: #50a5d1;*/
    color: #333;
    line-height: 60px;
    background-color: white;
    border-bottom: 1px solid #f1f1f1;
    box-shadow: 0px 0px 5px 0 rgba(0, 0, 0, .09) !important;
  }

  .el-aside {
    color: #333;
  }
  .header1 {
    height: 50px;
    position: relative;
    /*background-color: #f4f5ff;*/
    background: rgba(0, 136, 204, 0.05);
    color: #676767;
    /*border: 1px solid green;*/
  }

  .vertical-center {
    line-height: 60px;
    padding-left: 30px;
    margin: 0;
    position: absolute;
    top: 50%;
    -ms-transform: translateY(-50%);
    transform: translateY(-50%);
    color: #3A71A8;
  }


</style>
