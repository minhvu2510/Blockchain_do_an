<template>
    <div style="text-align: center;float: bottom">
        <el-steps :active="active" align-center finish-status="success">
            <el-step title="Bước 1" description="Xác nhận thông tin"></el-step>
            <el-step title="Bước 2" description="Hướng dẫn làm bài"></el-step>
            <el-step title="Bước 3" description="Giám thị nhập otp"></el-step>
            <el-step title="Bước 4" description="Bắt đầu làm bài"></el-step>
        </el-steps>
        <el-row :gutter="12" style="padding-top: 15px" v-show="active == 0" v-loading="loading">
            <el-col :span="7">
                <br/>
            </el-col>
            <el-col :span="10">
                <el-card shadow="always">
                    <center>
                        <img :src='link' alt="Smiley face" width="127" height="167">
                    </center>
                    <div>
                        <el-row style="padding-top: 15px">
                            <el-col :span="4">
                                <br/>
                            </el-col>
                            <el-col :span="6" style="text-align: left">
                                <b >Họ tên:</b>
                            </el-col>
                            <el-col :span="10" style="text-align: left">
                                <span>{{name}}</span>
                            </el-col>
                            <el-col :span="4">
                                <br/>
                            </el-col>
                        </el-row>
                        <el-row style="padding-top: 10px">
                            <el-col :span="4">
                                <br/>
                            </el-col>
                            <el-col :span="6" style="text-align: left">
                                <b>Ngày sinh:</b>
                            </el-col>
                            <el-col :span="10" style="text-align: left">
                                <span>{{born}}</span>
                            </el-col>
                            <el-col :span="4">
                                <br/>
                            </el-col>
                        </el-row>
                        <el-row style="padding-top: 10px">
                            <el-col :span="4">
                                <br/>
                            </el-col>
                            <el-col :span="6" style="text-align: left">
                                <b>Quê quán:</b>
                            </el-col>
                            <el-col :span="14" style="text-align: left">
                                <span>{{country}}</span>
                            </el-col>
                            <!--<el-col :span="4">-->
                                <!--<br/>-->
                            <!--</el-col>-->
                        </el-row>
                        <el-row style="padding-top: 10px">
                            <el-col :span="4">
                                <br/>
                            </el-col>
                            <el-col :span="6" style="text-align: left">
                                <b>Mã dự thi:</b>
                            </el-col>
                            <el-col :span="10" style="text-align: left">
                                <span>{{contest_code}}</span>
                            </el-col>
                            <el-col :span="4">
                                <br/>
                            </el-col>
                        </el-row>
                        <el-row style="padding-top: 10px">
                            <el-col :span="4">
                                <br/>
                            </el-col>
                            <el-col :span="16" style="text-align: left">
                                <!--<el-checkbox v-model="checked">Đã xác nhận thông tin!</el-checkbox>-->
                                <span style="color: #9a9e9f">Nếu thông tin sai vui lòng báo với giám thị!</span>
                            </el-col>
                            <el-col :span="2">
                                <br/>
                            </el-col>
                            <el-col :span="2">
                                <br/>
                            </el-col>
                        </el-row>
                        <el-row style="padding-top: 10px">
                            <el-col :span="4">
                                <br/>
                            </el-col>
                            <el-col :span="12" style="text-align: left">
                                <el-checkbox v-model="checked">Đã xác nhận thông tin!</el-checkbox>
                                <!--<span style="color: #9a9e9f">Xác nhận lại thông tin!</span>-->
                            </el-col>
                            <el-col :span="4">
                                <br/>
                            </el-col>
                            <el-col :span="4">
                                <br/>
                            </el-col>
                        </el-row>
                        <el-row v-show="checked">
                            <center style="padding-top: 15px">
                                <el-button type="success" @click="next" plain>Tiếp tục</el-button>
                            </center>
                        </el-row>

                    </div>
                </el-card>
            </el-col>
            <el-col :span="7">
                <br/>
            </el-col>
        </el-row>
        <el-row :gutter="12" style="padding-top: 15px" v-show="active == 1">
            <el-col :span="7">
                <br/>
            </el-col>
            <el-col :span="10">
                <el-card shadow="always">
                    <div>
                        <el-row style="padding-top: 15px">
                            <el-col :span="4">
                                <br/>
                            </el-col>
                            <el-col :span="16" style="text-align: left">
                                <b >Bài thi gồm 50 câu hỏi và 4 đáp án trả lời, chọn đáp án mà bạn cho là đúng nhất. Thời gian làm bài 45 phút. Hết thời gian hệ thống sẽ tự động nộp bài</b>
                            </el-col>
                            <el-col :span="4">
                                <br/>
                            </el-col>
                        </el-row>
                        <el-row style="padding-top: 10px">
                            <el-col :span="4">
                                <br/>
                            </el-col>
                            <el-col :span="12" style="text-align: left">
                                <el-checkbox v-model="checked2">Đã hiểu!</el-checkbox>
                                <!--<span style="color: #9a9e9f">Xác nhận lại thông tin!</span>-->
                            </el-col>
                            <el-col :span="4">
                                <br/>
                            </el-col>
                            <el-col :span="4">
                                <br/>
                            </el-col>
                        </el-row>
                        <el-row v-show="checked2">
                            <center style="padding-top: 15px">
                                <el-button type="success" @click="next" plain>Tiếp tục</el-button>
                            </center>
                        </el-row>

                    </div>
                </el-card>
            </el-col>
            <el-col :span="7">
                <br/>
            </el-col>
        </el-row>
        <el-row :gutter="12" style="padding-top: 55px" v-show="active == 2">
            <el-col :span="7">
                <br/>
            </el-col>
            <el-col :span="10">
                <el-card shadow="always">
                    <div>
                        <el-row style="padding-top: 15px">
                            <el-col :span="4">
                                <br/>
                            </el-col>
                            <el-col :span="16" style="text-align: left">
                                <el-input @keyup.enter.native="send_otp" placeholder="Please input otp" v-model="otp"></el-input>
                            </el-col>
                            <el-col :span="4">
                                <br/>
                            </el-col>
                        </el-row>
                        <el-row style="padding-top: 15px">
                            <span style="color: #9da3a8">Phần nhập mã otp của giám thị</span>
                        </el-row>
                        <el-row v-show="checked2">
                            <center style="padding-top: 15px">
                                <el-button type="success" @click="send_otp" plain>Tiếp tục</el-button>
                            </center>
                        </el-row>

                    </div>
                </el-card>
            </el-col>
            <el-col :span="7">
                <br/>
            </el-col>
        </el-row>
        <el-row :gutter="12" style="padding-top: 55px" v-show="active == 3">
            <el-col :span="7">
                <br/>
            </el-col>
            <el-col :span="10">
                <el-card shadow="always">
                    <div>
                        <!--<el-row :gutter="12">-->
                            <!--<el-col :span="8">-->
                                <!--<el-card shadow="hover">-->
                                    <!--<center>Tiếng anh</center>-->
                                <!--</el-card>-->
                            <!--</el-col>-->
                            <!--<el-col :span="8">-->
                                <!--<el-card shadow="hover">-->
                                    <!--<center>Toán</center>-->
                                <!--</el-card>-->
                            <!--</el-col>-->
                            <!--<el-col :span="8">-->
                                <!--<el-card shadow="hover">-->
                                    <!--<center>Ngữ văn</center>-->
                                <!--</el-card>-->
                            <!--</el-col>-->
                        <!--</el-row>-->
                        <!--<el-row>-->
                            <!--<center style="padding-top: 15px">-->
                                <!--<el-button type="success" @click="next" plain>Bắt đầu làm bài</el-button>-->
                            <!--</center>-->
                        <!--</el-row>-->
                        <el-row :gutter="20" style="margin-left: 0!important; margin-right: 0!important; margin-top: 30px">
                            <h3>Chọn môn thi</h3>
                            <br>
                            <el-col :span="8" v-for="ad in pack" :key="ad.id">
                                <center>
                                    <el-card class="box-style" @click.native="selectPack(ad)" :class="{'style-select': ad.check}">
                                        <center>{{ad.name}}</center>
                                    </el-card>
                                </center>
                            </el-col>
                        </el-row>
                        <el-row>
                            <center style="padding-top: 15px">
                                <el-button type="success" @click="start_exam" plain>Bắt đầu làm bài</el-button>
                            </center>
                        </el-row>

                    </div>
                </el-card>
            </el-col>
            <el-col :span="7">
                <br/>
            </el-col>
        </el-row>

    </div>
</template>

<script>
    import { getToken } from '@/utils/auth'
    import { getinfo } from '@/api/questions'
    export default {
        name: "confirm",
        data() {
            return {
                imgs:['https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSI4c7OFMNmQBqvoUzjbevUtsN9qsLkKVJ7sdD7pFglfMuTxk6G6w&s',
                    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRgvX0aDr7sAGjW8xYddoCqLnXcnhuMmkpttv1eu7dk-DaMho0q&s',
                'https://toplist.vn/images/800px/trung-tam-anh-mau-hoang-tram-319533.jpg',
                'https://photo-2-baomoi.zadn.vn/w1000_r1/2019_06_13_180_31074469/c8af53725632bf6ce623.jpg',
                'https://toplist.vn/images/800px/tiem-chup-anh-the-lay-ngay-dep-nhat-pleiku-gia-lai-chu-de-da-duoc-nhan-tran-minh-phuong-318152.jpg',
                'https://www.ruaanhgiare.com/wp-content/uploads/2018/03/anh-the-3x4.jpg'],
                checked: false,
                checked2: false,

                active: 0,
                otp: '',
                pack: [{'id': 1, 'name': 'Toán','check': false},
                        {'id': 2, 'name': 'Vật lý','check': false},
                    {'id': 3, 'name': 'Tiếng anh','check': false}],
                name: '',
                born: '',
                country: '',
                contest_code: '',
                // img: '../../assets/anhthe.jpeg'
                img: '',
                loading: true,
                link: ''
            }
        },
        mounted() {
            this.img = this.imgs[Math.floor(Math.random()*this.imgs.length)];
            // this.all_info()
            this.get_all_info()
        },
        methods: {
            next() {
                if (this.active++ > 2) this.active = 0;
            },
            selectPack(ad) {
                this.name = ad.name
                this.id = ad.id
                if (ad.check === false) {
                    ad.check = true
                    for (const i in this.pack) {
                        if (this.pack[i].id !== ad.id) {
                            this.pack[i].check = false
                        }
                    }
                }
            },
            send_otp () {
                this.axios.post( process.env.BASE_API +'/login', {
                    otp: this.otp,
                    step_2: 'yes',
                    token: getToken()
                }).then( (data) => {
                    if(data.data.status == true) {
                        this.$store.dispatch('gotAccessTokenOtp', data.data.token_otp).then(res=> {
                            console.log(data.data)
                            if (this.active++ > 2) this.active = 0;
                            // this.get_user_info()
                            // this.$router.push('/confirm')
                        })
                    }
                    // console.log(data)
                    // this.$store.dispatch('gotAccessToken', data.data.access_token).then(res=> {
                    //     this.get_user_info()
                    //     this.$router.push('/dashboard')
                    // })
                    // console.log('token is set to:',  this.$store.state.token)
                }, respone => {
                    this.$notify({
                        title: 'Error',
                        message: respone,
                        type: 'error'
                    })
                    // this.notify('info', respone.body.message)
                })},
            start_exam() {
                this.$router.push('/')
            },
            all_info() {
                // const param = {page: 1, limit: 100}
                this.axios.get( process.env.FAB_URL +'/api/query/' + this.$store.getters.id, {
                }).then( (data) => {
                    console.log('mvmvm')
                    console.log(data)
                    var res = JSON.parse(data.data.response)
                    console.log(res)
                    this.name = res.HoTen
                    this.born = res.NgaySinh
                    this.country = res.DiaChi
                    this.contest_code = res.MaDuThi
                }, respone => {
                    this.$notify({
                        title: 'Error',
                        message: respone,
                        type: 'error'
                    })
                    // this.notify('info', respone.body.message)
                })
            },
            get_all_info() {
                const data = {
                    user_id: this.$store.getters.id
                }
                getinfo(data)
                    .then(ress => {
                        console.log('-----------------')
                        // console.log(ress)
                        var res = (ress.data.data)
                        console.log(res)
                        // var res = JSON.parse(resi)
                        // console.log(res.response)
                        console.log(res)
                        console.log(res.HoTen)
                        this.name = res.HoTen
                        this.born = res.NgaySinh
                        this.country = res.DiaChi
                        this.contest_code = res.MaDuThi

                        this.link = res.link
                        this.loading = false
                        // if(res.data.status === 'ok') {
                        //     var dem = 0;
                        //     this.questions = res.data.data
                        //     for( var i in this.questions) {
                        //         dem += 1;
                        //         // console.log(res.data.data[i])
                        //         this.questions[i]['selec'] = 'Chưa trả lời'
                        //         this.questions[i]['index'] = dem
                        //         var data = {'idi': this.questions[i].idi, 'ans': 'Chưa trả lời', 'index': dem, 'result': ''}
                        //         this.table_answer.push(data)
                        //         // this.questions.push("dm")
                        //     }
                        //
                        // }
                        // console.log(this.questions)
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
            }
        }
    }
</script>

<style scoped>
    .title-style {
        font-size: 1em;
        font-weight: 700;
        color: #676767;
    }
    .add-hotline-form {
    .el-card__header {
        padding: 10px 20px !important;
        text-align: center !important;
        font-size: 16px;
        color: #000;
    }
    .el-card__body {
        text-align: center;
        font-size: 12px;
    .price-cover {
        margin-top: 0;
        color: #3A71A8;
    .price {
        font-size: 24px;
    }
    }
    }
    }
    .box-style{
        text-align: center;
        cursor: pointer;
        border: 1px solid #f1f1f1;
        color: #6e6e71;
        padding: 1.20rem;
    }
    .style-select {
        background: rgba(0, 136, 204, 0.05);
        border: 1px solid #0088cc;
        color: #676767;
    .el-card__body {
    .price-cover {
        color: #0088cc;
    }
    }
    }
    .hotline-info .el-card__body {
        padding-top: 0;
        padding-bottom: 0
    }
    .item{
        /*margin-top: 1.5em;*/
        padding: 1.2em 0 1em 0;
        border-bottom: 1px solid #f4f4f5;
    }
    .text {
        font-weight: bold;
        padding-left: 80px;
        font-size: 18px;
    }
</style>
