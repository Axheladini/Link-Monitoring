$(document).ready(function() 
{


    var all_pages = result[0]

    $.each(all_pages, function(i, item)
              {
                  var lang_holder = '<div class="container lch_'+item.code+'_container lang_container"><div class="row lan_name lang_flag"><div class="col-3"><h5>'+item.name+'</h5></div><div class="col-1 flag place '+item.code+'"></div></div></div>';
                  $('.lch_info_holder').append(lang_holder)

                  $.each(item.pages, function(p, page)
                  {
                        
                      var page_title = ' <div class="row lch_page_title"><div class="col-3"><h6> '+page.name+' - page</h6></div></div>';
                      var desc_row = '<div class="row details_row"><div class="col-2 d-flex align-items-center">Link Name</div><div class="col-8 d-flex align-items-center">Links to compare</div><div class="col-1 d-flex align-items-center">HTTP</div><div class="col-1 d-flex align-items-center">Details</div></div>'
                      $('.lch_'+item.code+'_container').append(page_title)
                      $('.lch_'+item.code+'_container').append(desc_row)

                  
                      $.each(page.links, function(l, link)
                      {   
                           if(link.status == 2 || link.status == 3 || link.status == 0) { var status = "red"; var found_color = "red"} else { status = "green"; found_color = "#cccccc"}
                           var link_row = '<div class="row lch_scan_details"><div class="col-2 d-flex align-items-center" style="text-align: left !important;">'+link.link_text+'</div><div class="col-8" style="word-wrap: break-word !important;"><u>link to find:</u> '+link.link_url+'<br> <span style="color:'+found_color+'"><i><u>link found:</u>   '+link.link_url_found+'</i></span></div><div class="col-1 d-flex align-items-center '+status+'"><span class="status_code">'+link.http_status+'</></div><div class="col-1 d-flex align-items-center"><span class="check_details"> Details</span></div><div class="col-12 detailed_message">'+link.link_message+'</div></div>';
                           $('.lch_'+item.code+'_container').append(link_row)

                      });

                  });
             });



    $('.lch_info_holder').on('click','.check_details', function()
{
     

     $(this).parent().next(".detailed_message").slideToggle('slow');

     if($(this).text() == 'Close')
       {
           $(this).text('Details');
           $(this).removeClass( "close" );
       }
       else
       {
           $(this).text('Close');
           $(this).addClass( "close" );
       }     
     
     
 });

});