$(document).ready(function(){
	"use strict";
    
        /*==================================
* Author        : "ThemeSine"
* Template Name : Listrace directory HTML Template
* Version       : 1.0
==================================== */




/*=========== TABLE OF CONTENTS ===========
1. Scroll To Top 
2. slick carousel
3. welcome animation support
4. feather icon
5. counter
======================================*/

    // 1. Scroll To Top 
		$(window).on('scroll',function () {
			if ($(this).scrollTop() > 600) {
				$('.return-to-top').fadeIn();
			} else {
				$('.return-to-top').fadeOut();
			}
		});
		$('.return-to-top').on('click',function(){
				$('html, body').animate({
				scrollTop: 0
			}, 1500);
			return false;
		});
	
	
	// 2. slick carousel

	    $(".testimonial-carousel").slick({
	        infinite: true,
	        centerMode: true,
	        autoplay:true,
	        slidesToShow: 5,
	        slidesToScroll: 3,
	        autoplaySpeed:1500,
	        // the magic
			responsive: [
				{

					breakpoint:1440,
					settings: {
					slidesToShow:3
					}

				},
				{

					breakpoint: 1024,
					settings: {
					slidesToShow:2,
					
					}

				}, 
				{

					breakpoint:991,
					settings: {
					slidesToShow:2,
					centerMode:false,
					}

				},
				{

					breakpoint:767,
					settings: {
					slidesToShow:1,
					}

				}
			]
	    });



    // 3. welcome animation support

        $(window).load(function(){
        	$(".welcome-hero-txt h2,.welcome-hero-txt p").removeClass("animated fadeInUp").css({'opacity':'0'});
            $(".welcome-hero-serch-box").removeClass("animated fadeInDown").css({'opacity':'0'});
        });

        $(window).load(function(){
        	$(".welcome-hero-txt h2,.welcome-hero-txt p").addClass("animated fadeInUp").css({'opacity':'0'});
            $(".welcome-hero-serch-box").addClass("animated fadeInDown").css({'opacity':'0'});
        });

		
		//----------------------------------------------------------------
		$(window).load(function(){
        	$(".tenders-hero-txt h2,.tenders-hero-txt p").removeClass("animated fadeInUp").css({'opacity':'0'});
            $(".tenders-hero-serch-box").removeClass("animated fadeInDown").css({'opacity':'0'});
        });

        $(window).load(function(){
        	$(".tenders-hero-txt h2,.tenders-hero-txt p").addClass("animated fadeInUp").css({'opacity':'0'});
            $(".tenders-hero-serch-box").addClass("animated fadeInDown").css({'opacity':'0'});
        });

	// 4. feather icon

		feather.replace();

	// 5. counter
		$(window).on('load', function(){	
			$('.counter').counterUp({
				delay: 10,
				time: 3000
			});	
		});

});



document.addEventListener('DOMContentLoaded', function () {
    const ministryField = document.getElementById('id_ministry');
    const departmentField = document.getElementById('id_department');
    const locationField = document.getElementById('id_regionstate');
    const cityField = document.getElementById('id_city');

    ministryField.addEventListener('change', function () {
        const ministryId = ministryField.value;
        if (ministryId) {
            fetch(`/api/departments/${ministryId}/`)
                .then(response => response.json())
                .then(data => {
                    departmentField.innerHTML = '';
                    data.forEach(department => {
                        const option = document.createElement('option');
                        option.value = department.id;
                        option.textContent = department.name;
                        departmentField.appendChild(option);
                    });
                });
        }
    });

    locationField.addEventListener('change', function () {
        const locationId = locationField.value;
        if (locationId) {
            fetch(`/api/cities/${locationId}/`)
                .then(response => response.json())
                .then(data => {
                    cityField.innerHTML = '';
                    data.forEach(city => {
                        const option = document.createElement('option');
                        option.value = city.id;
                        option.textContent = city.name;
                        cityField.appendChild(option);
                    });
                });
        }else {
            cityField.innerHTML = '<option value="">---------</option>';
        }
    });
});