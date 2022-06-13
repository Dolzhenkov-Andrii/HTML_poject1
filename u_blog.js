let our_blog = [
    {
        img_link: "blog_img/bimg_1.png",
        title: "Pellentesque felis nibh",
        article: "Phasellus sit amet neque molestie nunc tincidunt ultrices. Donec laoreet mi sit amet gravida bibendum. Aliquam erat volutpat. Aliquam arcu est, malesuada a nisi in.",
    },
    {
        img_link: "blog_img/bimg_2.png",
        title: "Mauris nisi magna, congue quis faucibus ac",
        article: "Nulla in tincidunt neque, a luctus mi. Donec sollicitudin est vehicula mauris condimentum mattis. Suspendisse in augue ut lorem viverra dignissim. Fusce ultrices, mauris vitae fringilla.",
    },
    {
        img_link: "blog_img/bimg_3.png",
        title: "Adipiscing auctor turpis",
        article: "Aenean auctor leo et libero convallis, eget tempor urna rutrum. Aliquam erat volutpat. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.",
    },
    {
        img_link: "blog_img/bimg_4.png",
        title: "Duis sed lectus placerat, facilisis lacus id",
        article: "Pellentesque aliquam eros non augue cursus, ut porta leo ornare. Suspendisse odio lectus, commodo ac mauris in, bibendum pretium nisi.",
    },
    {
        img_link: "blog_img/bimg_5.png",
        title: "Fermentum pellentesque dolor at",
        article: "Duis eros nisl, tincidunt sed elit ut, feugiat elementum justo. Vivamus ornare id eros vel imperdiet. Sed venenatis dapibus consequat. Curabitur viverra erat id vehicula consectetur.",
    },
    {
        img_link: "blog_img/bimg_6.png",
        title: "Nunc sodales nec ante eget sollicitudin",
        article: "Pellentesque imperdiet sem nec pellentesque luctus. Sed nisl elit, tempus sed ultricies vel, laoreet ut magna. In a condimentum nulla. Maecenas sem tellus, blandit a felis at, luctus lobortis erat.",
    },
    
];
$(document).ready(function(){

if(our_blog.length > 0){
    for (let i = 0; i < our_blog.length && i < 6; i++){
        $(`.ourBlogs:eq(${i})`).addClass("notNull");
        $(`.ob_img${i}`).css("content", `url(${our_blog[i].img_link}`);
        $(`#ob_title${i}`).text(our_blog[i].title);
        $(`#ob_text${i}`).text(our_blog[i].article);
        $(`#ob_fullLink${i}`).text("Read more");
    }
} else {
    $(`.our_blogs`).text("sorry blog-list is empty");
    $(`.our_blogs`).css("font-size", "50px");
    $(`.our_blogs`).css("font-weight","600");
    $(`.our_blogs`).css("text-transform","uppercase");
    $(`.our_blogs`).css("justify-content","center");
    $(`.our_blogs`).css("padding-top","150px");
}
});
