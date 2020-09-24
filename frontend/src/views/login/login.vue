<template>
    <!--<div style="margin-top: -45px">-->
    <div>
        <!--<div style="padding-bottom: 15px">-->
            <!--<h2>Kỳ thi tuyển sinh đại học</h2>-->
        <!--</div>-->

        <div class="limiter">
            <div class="container-login100" style="margin-top: -65px">
                <div class="wrap-login100">
                    <div class="login100-form validate-form">
                        <div style="padding-bottom: 15px; border-radius: 5%">
                            <img style="border-radius: 10%" src="../../../public/images/ptit.jpeg" width="225" height="175">
                        </div>
					<span class="login100-form-title p-b-43" style="font-family: Helvetica, sans-serif">
						Đăng nhập để làm bài thi
					</span>


                        <div class="wrap-input100 validate-input" data-validate = "Valid email is required: ex@abc.xyz">
                            <!--<input class="input100" type="text" name="email">-->
                            <input class="input100" v-model="username" type="text" name="username" >
                            <span class="focus-input100"></span>
                            <span class="label-input100">Mã dự thi</span>
                        </div>


                        <div v-if="disPass==false" class="wrap-input100 validate-input" data-validate="Password is required">
                            <input @keyup.enter.native="login" v-model="password" class="input100" type="password" name="pass">
                            <span class="focus-input100"></span>
                            <span class="label-input100">Mật khẩu</span>
                        </div>
                        <div v-else class="wrap-input100 validate-input" data-validate="Password is required">
                            <input @keyup.enter.native="login" v-model="password" class="input100" type="text" name="pass">
                            <span class="focus-input100"></span>
                            <span class="label-input100">Mật khẩu</span>
                        </div>

                        <div class="flex-sb-m w-full p-t-3 p-b-32">
                            <div class="contact100-form-checkbox">
                                <input v-model="disPass" class="input-checkbox100" id="ckb1" type="checkbox" name="remember-me">
                                <label class="label-checkbox100" for="ckb1" style="font-family: Helvetica, sans-serif">
                                    Hiển thị mật khẩu
                                </label>
                            </div>

                            <!--<div>-->
                                <!--<a href="#" class="txt1">-->
                                    <!--Forgot Password?-->
                                <!--</a>-->
                            <!--</div>-->
                        </div>


                        <div class="container-login100-form-btn">
                            <button class="login100-form-btn" @click="login">
                                Đăng nhập
                            </button>
                        </div>

                        <div class="text-center p-t-46 p-b-20">
						<span class="txt2">
							Vui lòng làm theo hướng dẫn của giám thị
						</span>
                        </div>
                    </div>

                    <div class="login100-more">

                        <div style="width: 100%;height: auto; background-color: rgba(240,108,108,0.21)">
                            <p class="term">* Quy chế thi ( những điều cần lưu ý ):</p>
                            <p class="item">1. Không mang tài liệu vào phòng thi</p>
                            <p class="item">2. Không trao đổi trong phòng thi, nếu vi phạm sẽ bị khóa tài khoản</p>
                            <p class="item">3. Mỗi tài khoản chỉ đăng nhập được một lần.</p>
                            <p class="item">4. Sau khi đăng nhập, thí sinh kiểm tra thông tin, nếu sai báo với giám thị</p>
                            <p class="item">5. Tại giao diện làm bài sẽ có thời gian làm bài, sau khi hết thời gian bài làm sẽ tự động nộp</p>
                        </div>
                        <div >
                            <el-carousel height="450px"  :interval="1500" arrow="always">
                                <el-carousel-item v-for="item in 6" :key="item">
                                    <!--<h3>{{ item }}</h3>-->
                                    <!--<div class="login100-more" style="background-image: url('images/thpt5.jpg');"></div>-->
                                </el-carousel-item>
                            </el-carousel>
                        </div >
                        <!--<h3 class='txtinsetshadow' style="font-family: Helvetica, sans-serif; color: red;padding-top: 30px">Bình tĩnh - Tự tin - Chiến thắng</h3>-->
                        <el-alert
                                style="font-family: Helvetica, sans-serif;"
                                center
                                title="Bình tĩnh - Tự tin - Chiến thắng"
                                type="success"
                                description="Đây là những giờ phút vô cùng quan trọng của cuộc đời, hãy tập trung và đừng để bất cứ điều gì làm xao nhãng bạn nhé."
                                :closable="false">
                        </el-alert>
                        <el-alert
                                style="font-family: Helvetica, sans-serif;"
                                center
                                type="success"
                                description="Chúc các em có một kỳ thi thật tốt! Đừng tạo áp lực cho mình, cứ để tâm trí bình thản, đừng quá căng thẳng,...cứ thư giản nhé rồi em sẽ có một kỳ thi thật tốt cho xem! Các cá chép đang đợi hóa rồng hãy cố gắng lên nhé, mọi người lun sát cánh bên các em.Chúc các sĩ tử thi thật tốt và cho dù có không tốt thì cũng sẽ có một lối đi thích hợp cho mình.
Cố gắng lên nhé!"
                                :closable="false">
                        </el-alert>
                    </div>

                </div>
            </div>
        </div>

    </div>
</template>

<script>
    export default {
        name: "login",
        data() {
            return {
                username: '',
                password: '',
                he: '50000',
                disPass: false
            }
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
            login () {
                this.axios.post( process.env.BASE_API +'/login', {
                    username: this.username,
                    password: btoa(this.password),
                    step_1: 'yes'
                }).then( (data) => {
                    if(data.data.status == true) {
                        this.$store.dispatch('GetUserInfo', this.username).then(res=> {
                            console.log('mvmvm')
                            // console.log(data.data)
                            // this.get_user_info()
                            // this.$router.push('/confirm')
                        })
                        this.$store.dispatch('SetAction', this.username).then(res=> {
                            console.log('mvmvm')
                            // console.log(data.data)
                            // this.get_user_info()
                            // this.$router.push('/confirm')
                        })
                        this.$store.dispatch('gotAccessToken', data.data.token).then(res=> {
                            console.log(data.data)
                            // this.get_user_info()
                            this.$router.push('/confirm')
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
                        title: 'Lỗi',
                        message: 'Nếu không đăng nhập được vui lòng liên hệ giám thị',
                        type: 'error'
                    })
                    // this.notify('info', respone.body.message)
                })},
            register() {
                this.$router.push('/register')
            }
        }
    }
</script>
<!--===============================================================================================-->

<style>
    .el-carousel__item h3 {
        color: #de2311;
        font-size: 18px;
        opacity: 0.75;
        line-height: 90%;
        margin: 0;
    }

    .el-carousel__item:nth-child(n) {
        background-color: #99a9bf;
        background-image: url("https://portal.ptit.edu.vn/wp-content/uploads/2019/01/ptit.jpg");
    }

    /*.el-carousel__item:nth-child(2n+1) {*/
        /*background-color: #d3dce6;*/
        /*background-image: url("https://congly.vn/data/news/2018/6/24/176/ngam-nu-cuoi-rang-ngoi-cua-nu-sinh-10x-tai-ky-thi-thpt-quoc-gia-2018-hinh-anh11375863980.jpg");*/
    /*}*/
    /*.el-carousel__item:nth-child(2n) {*/
        /*background-color: #d3dce6;*/
        /*background-image: url("https://media-giaoducthoidai.cdn.vccloud.vn/Uploaded/nhungnt/2019-06-04/thi-thpt-quoc-gia-JNFY.jpg");*/
    /*}*/

    .txtinsetshadow {
        text-align: center;
        font-size: 40px;
        height: 100px;
        padding-top: 40px;
        color: #202020;
        /*background-color: #2d2d2d;*/
        letter-spacing: .1em;
        text-shadow: -1px -1px 1px #111, 2px 2px 1px #363636;
    }
    .term {
        font-family: Palatino;
        font-size: 16px;
        color: red;
        font-weight: bold;
        padding-top: 7px;
        text-align: left;
        padding-left: 7px;
    }
    .item {
        font-family: Palatino;
        color: rgba(255, 0, 0, 0.57);
        font-size: 14px;
        text-align: left;
        padding-left: 7px;
    }
</style>
