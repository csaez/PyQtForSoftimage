##
#	\namespace	[package].[class::lower]
#
#	\remarks	The main View class for the [name] Trax View
#	
#	\author		beta@blur.com
#	\author		Blur Studio
#	\date		[date]
#

from PyQt4.QtGui import QWidget

class [class]( QWidget ):
	def __init__( self, parent ):
		QWidget.__init__( self, parent )
		
		# load the ui
		import blurdev.gui
		blurdev.gui.loadUi( __file__, self )
		
		# create connections