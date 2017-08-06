/**
 * Created by Administrator on 2017/7/18 0018.
 */
    //列表切换
    $(document).ready(function() {

        //Default Action
        $(".tab_content").hide(); //Hide all content
        $("ul.tabs li:first").addClass("active").show(); //Activate first tab
        $(".tab_content:first").show(); //Show first tab content

        //On Click Event
        $("ul.tabs li").click(function() {
            $("ul.tabs li").removeClass("active"); //Remove any "active" class
            $(this).addClass("active"); //Add "active" class to selected tab
            $(".tab_content").hide(); //Hide all tab content
            var activeTab = $(this).find("a").attr("href"); //Find the rel attribute value to identify the active tab + content
            $(activeTab).fadeIn(); //Fade in the active content
            var newHeight = $(activeTab).height();
            console.log(newHeight);
            $(".tab_container").css("height",newHeight);
            $(".tabs").css("height",newHeight);
            return false;
        });



        //tab1-基本信息 上传图片预览
        var
            fileInput = document.getElementById('test-image-file'),
            preview = document.getElementById('test-image-preview');
        // 监听change事件:
        fileInput.addEventListener('change', function () {
            // 清除背景图片:
            preview.style.backgroundImage = '';
            // 检查文件是否选择:
            if (!fileInput.value) {
                info.innerHTML = '没有选择文件';
                return;
            }
            // 获取File引用:
            var file = fileInput.files[0];
            // 读取文件:
            var reader = new FileReader();
            reader.onload = function(e) {
                var
                    data = e.target.result; // 'data:image/jpeg;base64,/9j/4AAQSk...(base64编码)...'
                preview.style.backgroundImage = 'url(' + data + ')';
            };
            // 以DataURL的形式读取文件:
            reader.readAsDataURL(file);
        });


        //tab2-发布房源
        //增加卧室
        var roomHeight = $('.bedroom').height();
        $('.addBedroom').click(function () {
            var newBedroom = document.createElement('div');
            console.log(newBedroom);
            newBedroom.className = 'bedroom';
            newBedroom.innerHTML = '<h5>卧室</h5><p><label>面积：</label><input class="area" type="text">&nbsp m³</p><p>房间配置：<label>飘窗 </label><input type="checkbox" name="details">&nbsp&nbsp<label>空调 </label><input type="checkbox" name="details">&nbsp&nbsp<label>床 </label><input type="checkbox" name="details">&nbsp&nbsp<label>书桌 </label><input type="checkbox" name="details">&nbsp&nbsp<label>衣柜 </label><input type="checkbox" name="details">&nbsp&nbsp<label>沙发 </label><input type="checkbox" name="details">&nbsp&nbsp<label>卫生间 </label><input type="checkbox" name="details"></p><span class="close">X</span>';
            $('.addBedroom').before(newBedroom);
            $(".tab_container").css("height",$(".tab_container").height() + roomHeight);
            $(".tabs").css("height",$(".tab_container").height());
            console.log($('.bedroom'));
        });

        //客厅
        if($('#yes').checked){

        }
        //删除卧室
        $(document).on('click','.house-release .bedroom .close',(function () {
            this.parentNode.parentNode.removeChild(this.parentNode);
            $(".tab_container").css("height",$(".tab_container").height() - roomHeight);
            $(".tabs").css("height",$(".tab_container").height());
        }));

        //tab3-房源管理

        //tab4-房源发布
        //日历
        $(document).ready(function () {
            $('#selectDate').datepicker({
                dateFormat: 'yy-mm-dd',
                monthNames: ['一月','二月','三月','四月','五月','六月','七月','八月','九月','十月','十一月','十二月']
            });
        });
        //手机验证
        var inp = document.getElementById('phoneNum');
        inp.onfocus = function () {
          this.select();
        };
        inp.onblur = function () {
            console.log(11);
            var reg1 = /^(13[0-9]|15[0|3|6|7|8|9]|18[8|9])\d{8}$/;
            if(reg1.test(inp.value)){
                //3、符合个给一个样式，不符合给另一个样式
                inp.style.color = "green";
            }else{
                inp.style.color = "red";
                inp.value = inp.value+"  请输入正确的手机号码";
            }
        };

        // tab6 房源管理
        $(function () {
            var wjx_none = "☆";
            var wjx_sel = "★";
            //需求1：鼠标放上去  当前的li和之前所有的li内容全部变为实心五角星，其他空心，离开变为空心
            //需求2：鼠标点击哪个li，当前的li和之前的所有li变为实心，其他变为空心

            //需求1：鼠标放上去  当前的li和之前所有的li内容全部变为实心五角星，其他空心，离开变为空心
            $(".comment li").on("mouseenter",function () {
                //当前的li和之前所有的li内容全部变为实心五角星，其他空心
                $(this).text(wjx_sel).prevAll(".comment li").text(wjx_sel).end().nextAll(".comment li").text(wjx_none);
            });

            $(".comment li").on("mouseleave",function () {
                //bug：如果没有点击过li,那么会出现无法清除的现象
                if($("li.current").length === 0){
                    $(".comment li").text(wjx_none);
                }else {
                    $("li.current").text(wjx_sel).prevAll(".comment li").text(wjx_sel).end().nextAll(".comment li").text(wjx_none);
                }
                //当鼠标移开时， 哪个li有current的类名，该li及其前面的全部变为实心五角星，其他空心
            });

            //需求2：鼠标点击哪个li，当前的li和之前的所有li变为实心，其他变为空心
            $(".comment li").on("click",function () {
                //点击哪个li ，给哪个加一个类名。其他所有li的类名清空
//                $(this).text(wjx_sel).prevAll().text(wjx_sel).end().nextAll().text(wjx_none);
                $(this).attr("class","current").siblings(".comment li").removeAttr("class");
            })

        });

    });



