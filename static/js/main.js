const toggler = document.querySelector(".navbar__toggler");
const navbar = document.querySelector(".navbar");
toggler.addEventListener("click", (e) => {
    navbar.classList.toggle("nav__expanded");
});

var infinite = new Waypoint.Infinite({
    element: $('.infinite-container')[0],
    handler: function (direction) {

    },
    offset: 'bottom-in-view',

    onBeforePageLoad: function () {
        $('.spinner-border').show();
    },
    onAfterPageLoad: function () {
        $('.spinner-border').hide();
    }

});
CKEDITOR.replace('textarea');


function fillParentId(parentId) {
    $('#parent_id').val(parentId);
    document.getElementById('comment_form').scrollIntoView({behavior: "smooth"});
}
