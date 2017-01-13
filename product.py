#-*- coding:utf-8 -*-

from openerp.osv import osv, fields

class product_product(osv.osv):
	_inherit = "product.product"

	def name_search(self, cr, uid, name, args=None, operator='ilike', context=None, limit=100):
		"""Filter Products of selected Supplier in RFQ/PO
		"""
		if context and 'filter_partner_product' in context and 'bin_size' not in context:
			prod_ids = []
			partner_id = context['partner_id']
			products = self.pool.get('product.supplierinfo').search(cr, uid, [('name','=',partner_id)])
			for prod_supplier in self.pool.get('product.supplierinfo').browse(cr, uid, products):
				tmpl_id = prod_supplier.product_tmpl_id.id
				prod_id = self.pool.get('product.product').search(cr, uid, [('product_tmpl_id','=',tmpl_id)])
				prod_ids.append(prod_id)
			args = [['id', 'in', prod_ids]]
		return super(product_product,self).name_search(cr, uid, name, args, operator=operator, context=context, limit=limit)

