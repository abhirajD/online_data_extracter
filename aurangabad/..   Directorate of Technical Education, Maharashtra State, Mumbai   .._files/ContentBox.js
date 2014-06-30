/************************************************************************************************
Name		- Content Box
Description	- Client side functionalities of ContentBox.
Version		- 2.0.0
Author		- Anoop Nair.
Company		- OASIS (part of MKCL).

# COPYRIGHT NOTICE
# Copyright (c) 2005-2010 MKCL, All rights reserved.
# This script may be used and modified free of charge for Non-profit purposes by anyone as long
# as this copyright notice and the comments above are kept in their original form.
************************************************************************************************/

if(typeof(OASIS)=='undefined')
window.reload(true);OASIS.ContentBox=new function(){var images=new function(){this.upNorm=new Image();this.upGlow=new Image();this.dnNorm=new Image();this.dnGlow=new Image();this.close=new Image();};var supCol=false,ziValue=0;images.upNorm.src="../Images/ContentBox_up.gif";images.upGlow.src="../Images/ContentBox_upgw.gif";images.dnNorm.src="../Images/ContentBox_down.gif";images.dnGlow.src="../Images/ContentBox_downgw.gif";images.close.src="../Images/ContentBox_close.gif";function SuppressCollapsing(){supCol=true;}function ChangeStyle(contentBox){if(contentBox.ShrinkButton.src.EndsWith("upgw.gif"))contentBox.ShrinkButton.src=images.upNorm.src;else if(contentBox.ShrinkButton.src.EndsWith("up.gif"))contentBox.ShrinkButton.src=images.upGlow.src;else if(contentBox.ShrinkButton.src.EndsWith("downgw.gif"))contentBox.ShrinkButton.src=images.dnNorm.src;else if(contentBox.ShrinkButton.src.EndsWith("down.gif"))contentBox.ShrinkButton.src=images.dnGlow.src;if(document.body.style.cursor=='pointer')document.body.style.cursor='default';else document.body.style.cursor='pointer';}function ChangeDisplay(contentBox){if(supCol){supCol=false;return;}if(contentBox.InnerBody.style.display==''){contentBox.InnerBody.style.display='none';if(contentBox.ShrinkButton.src.EndsWith("gw.gif"))contentBox.ShrinkButton.src=images.dnGlow.src;else contentBox.ShrinkButton.src=images.dnNorm.src;}else{contentBox.InnerBody.style.display='';if(contentBox.ShrinkButton.src.EndsWith("gw.gif")!=-1)contentBox.ShrinkButton.src=images.upGlow.src;else contentBox.ShrinkButton.src=images.upNorm.src;}}function WindowScroll(contentBox){var move=OASIS.Browser.GetScrollPosition();move.Subtract(contentBox.cBox.scroll);if(move.X==0 && move.Y==0)return;if(!contentBox.cBox.moveX && !contentBox.cBox.moveY)return;MoveBox(contentBox,move);contentBox.cBox.scroll.Add(move);}function WindowResize(contentBox){var viewport=OASIS.Browser.GetViewport();ResetBox(contentBox,viewport,null);ResetOverlay(contentBox,viewport);}function MoveBox(contentBox,MoveRate){if(contentBox.cBox.moveY)contentBox.style.top=(parseInt(contentBox.style.top)+MoveRate.Y)+'px';if(contentBox.cBox.moveX)contentBox.style.left=(parseInt(contentBox.style.left)+MoveRate.X)+'px';}function ResetBox(contentBox,viewport,scroll){if(!viewport)viewport=OASIS.Browser.GetViewport();if(!scroll)scroll=OASIS.Browser.GetScrollPosition();contentBox.cBox.moveX=true;contentBox.cBox.moveY=true;var pos=new OASIS.Point(viewport.Width,viewport.Height);pos.Subtract(new OASIS.Point(contentBox.offsetWidth,contentBox.offsetHeight));if(pos.X< 0){pos.X=0;contentBox.cBox.moveX=false;}if(pos.Y< 0){pos.Y=0;contentBox.cBox.moveY=false;}contentBox.style.top=(scroll.Y+pos.Y/2- 4)+'px';contentBox.style.left=(scroll.X+pos.X/2)+'px';if(OASIS.Browser.IsIe && OASIS.Browser.Version <7){contentBox.cBox.olayFrm.style.top=(0- parseInt(contentBox.style.top)- 4)+'px';contentBox.cBox.olayFrm.style.left=(0 - parseInt(contentBox.style.left))+'px';}}function ResetOverlay(contentBox,viewport){if(!viewport)viewport=OASIS.Browser.GetViewport();contentBox.cBox.olayFrm.style.height=viewport.Height+'px';contentBox.cBox.olayFrm.style.width=viewport.Width+'px';contentBox.cBox.olayDiv.style.height=viewport.MaxHeight+'px';contentBox.cBox.olayDiv.style.width=viewport.MaxWidth+'px';}function SetBox(contentBox,zDisplay){contentBox.style.zIndex=103+zDisplay;var scroll=OASIS.Browser.GetScrollPosition();contentBox.cBox.scroll=scroll;if(OASIS.Browser.IsIe)document.body.childNodes[0].appendChild(contentBox);contentBox.style.display='block';ResetBox(contentBox,null,scroll);}function SetOverLay(contentBox,zDisplay){if(OASIS.Browser.IsIe){contentBox.cBox.olayFrm.style.filter='alpha(opacity=0)';contentBox.cBox.olayDiv.style.filter='alpha(opacity=60)';}else{contentBox.cBox.olayFrm.style.opacity=.0;contentBox.cBox.olayDiv.style.opacity=.6;}contentBox.cBox.olayFrm.style.zIndex=(OASIS.Browser.IsIe && OASIS.Browser.Version<7 ? -1: 101+zDisplay);contentBox.cBox.olayDiv.style.zIndex=102+zDisplay;document.body.appendChild(contentBox.cBox.olayDiv);contentBox.cBox.olayFrm.style.display='block';contentBox.cBox.olayDiv.style.display='block';ResetOverlay(contentBox);}function IeWidthSetHandler(contentBox){contentBox.InnerBody.style.width=contentBox.offsetWidth - 14;}function ShowWindow(contentBox,colorSelected,showClose,closeEventHandler){var zDisplay=ziValue++;zDisplay*=5;SetBox(contentBox,zDisplay);SetOverLay(contentBox,zDisplay);if(colorSelected)contentBox.cBox.olayDiv.style.background=colorSelected;contentBox.cBox.scrollEvent=setInterval(contentBox.id+".cBox.WindowScroll()",500);OASIS.FuncLib.AddEventHandler(window,'resize',contentBox.cBox.WindowResize);if(showClose){var lnk=document.createElement('A');var img=document.createElement('IMG');img.src=images.close.src;if(OASIS.Browser.IsIe)img.style.width="15px";lnk.appendChild(img);lnk.href="javascript:void(0);";if(closeEventHandler){OASIS.FuncLib.AddEventHandler(lnk,'click',function(){var e=new function(){this.ClosePopup=true;};closeEventHandler(contentBox,e);if(e.ClosePopup)contentBox.Hide();});}else{OASIS.FuncLib.AddEventHandler(lnk,'click',contentBox.Hide);}contentBox.Head.appendChild(lnk);}}function CloseWindow(contentBox){ziValue--;contentBox.style.display='none';contentBox.cBox.olayFrm.style.display='none';contentBox.cBox.olayDiv.style.display='none';clearInterval(contentBox.cBox.scrollEvent);OASIS.FuncLib.RemoveEventHandler(window,'resize',contentBox.cBox.WindowResize);}this.PrepareObject=function(contentBox,enableOverlay,enablePercentageWidth,enablePrinting,isPlinth){var boxId=contentBox.id;var panels=contentBox.getElementsByTagName('DIV');contentBox.IsPlinth=isPlinth;contentBox.cBox=new Object();contentBox.Head=panels.item(0);if(contentBox.Head.className=='HeadDiv'){contentBox.Body=panels.item(1);contentBox.InnerBody=panels.item(2);contentBox.ShrinkButton=contentBox.Head.getElementsByTagName('img').item(0);contentBox.Title=contentBox.Head.getElementsByTagName('SPAN')[0];contentBox.SetHeaderText=function(text){contentBox.Title.innerHTML=text;};contentBox.GetHeaderText=function(){return contentBox.Title.innerHTML;};}else{contentBox.Head=null;contentBox.Body=panels.item(0);contentBox.InnerBody=panels.item(1);contentBox.ShrinkButton=null;contentBox.Title=null;contentBox.SetHeaderText=function(text){};contentBox.GetHeaderText=function(){return 'NA';};}contentBox.SetWidth=function(newWidth){OASIS.ContentBox.BoxEvent('setwidth',contentBox,newWidth);};if(enableOverlay){contentBox.cBox.olayFrm=document.getElementById(boxId+'_ContentBoxOverlayOne');if(!contentBox.cBox.olayFrm){contentBox.cBox.olayFrm=new Object();contentBox.cBox.olayFrm.style=new Object();}contentBox.cBox.olayDiv=document.getElementById(boxId+'_ContentBoxOverlayTwo');contentBox.cBox.WindowScroll=function(){OASIS.ContentBox.BoxEvent('scroll',contentBox);};contentBox.cBox.WindowResize=function(){OASIS.ContentBox.BoxEvent('resize',contentBox);};contentBox.Show=function(newColor,showClose,closeEventHandler){OASIS.ContentBox.BoxEvent('show',contentBox,newColor,showClose,closeEventHandler);};contentBox.Hide=function(){OASIS.ContentBox.BoxEvent('close',contentBox);};}if(enablePercentageWidth){}if(enablePrinting){contentBox.Print=function(dontPrintHead){OASIS.ContentBox.PrintThis(contentBox,dontPrintHead);};}};this.BoxEvent=function(action,contentBox){switch(action){case 'show': ShowWindow(contentBox,arguments[2],arguments[3],arguments[4],arguments[5]);break;case 'close': CloseWindow(contentBox);break;case 'suppress': SuppressCollapsing();break;case 'dispChange': ChangeDisplay(contentBox);break;case 'styleChange': ChangeStyle(contentBox);break;case 'scroll': WindowScroll(contentBox);break;case 'resize': WindowResize(contentBox);break;case 'iewidth': IeWidthSetHandler(contentBox);break;case 'printbox': PrintBox(contentBox,arguments[2]);break;case 'printcnt': PrintContinued(contentBox);break;case 'setwidth': AssignNewWidth(contentBox,arguments[2]);break;}};this.PrintThis=function(contentBox){HideForPrint(contentBox);if(contentBox.Head){var links=contentBox.Head.getElementsByTagName('A');for(var i=0;i< links.length;i++)links[i].style.display='none';}window.print();if(OASIS.Browser.IsFirefox)setTimeout('OASIS.ContentBox.BoxEvent(\'printcnt\','+contentBox.id+')',950);else PrintContinued(contentBox);};function PrintBox(contentBox,dontPrintHead){if(dontPrintHead)OASIS.ContentBox.PrintThis(contentBox.InnerBody);else OASIS.ContentBox.PrintThis(contentBox);}function PrintContinued(contentBox){ShowAfterPrint(document.body);if(contentBox.Head){var links=contentBox.Head.getElementsByTagName('A');for(var i=0;i< links.length;i++)links[i].style.display='';}}function HideForPrint(elem){var parent=elem.parentNode;if(parent==null)return;for(var i=0;i< parent.childNodes.length;i++)if(parent.childNodes[i]!=elem && parent.childNodes[i].style!=null)if(parent.childNodes[i].style.display!='none'){parent.childNodes[i].HideForCBPrint='yes';parent.childNodes[i].style.display='none';}HideForPrint(parent);}function ShowAfterPrint(elem){for(var i=0;i< elem.childNodes.length;i++){if(typeof(elem.childNodes[i].HideForCBPrint)!='undefined'){elem.childNodes[i].style.display='';elem.childNodes[i].HideForCBPrint=null;}else{ShowAfterPrint(elem.childNodes[i]);}}}function AssignNewWidth(contentBox,newWidth){if(newWidth=='auto'){contentBox.style.width='auto';contentBox.InnerBody.style.width='auto';contentBox.Body.style.width='auto';return;}if(typeof(newWidth)!='number'){alert('ContentBox - Width should be "auto" or numeric!');return;}contentBox.style.width=newWidth+'px';if(contentBox.IsPlinth)newWidth-=10;contentBox.InnerBody.style.width=(newWidth- 12)+'px';contentBox.Body.style.width=(newWidth- 2)+'px';}};