def randomTagStyle(tagname):
    l=['default','primary','success','info','warning','danger']
    return '<span class="label label-'+l+'><a class="tag" href="/tag/'+tagname+'">'+[random()%6]+'>'+tagname+'</a></span>'