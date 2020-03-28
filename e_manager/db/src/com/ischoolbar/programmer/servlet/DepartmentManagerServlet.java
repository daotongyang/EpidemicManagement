package com.ischoolbar.programmer.servlet;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import net.sf.json.JSONArray;
import net.sf.json.JSONObject;

import com.ischoolbar.programmer.bean.Operator;
import com.ischoolbar.programmer.bean.Page;
import com.ischoolbar.programmer.bean.SearchProperty;
import com.ischoolbar.programmer.dao.DepartmentManagerDao;
import com.ischoolbar.programmer.dao.StudentDao;
import com.ischoolbar.programmer.entity.DepartmentManager;
import com.ischoolbar.programmer.entity.Student;
import com.ischoolbar.programmer.util.StringUtil;
/**
 * 宿舍管理员管理
 * @author llq
 *
 */
public class DepartmentManagerServlet extends HttpServlet {
	/**
	 * 
	 */
	private static final long serialVersionUID = -4065921699848849543L;

	protected void doGet(HttpServletRequest req, HttpServletResponse resp)
			throws ServletException, IOException {
		// TODO Auto-generated method stub
		doPost(req, resp);
	}

	@Override
	protected void doPost(HttpServletRequest req, HttpServletResponse resp)
			throws ServletException, IOException {
		String method = req.getParameter("method");
		if("toDormitoryManagerListView".equals(method)){
			req.getRequestDispatcher("view/dormitoryManagerList.jsp").forward(req, resp);
		}
		if("AddDormitoryManager".equals(method)){
			addDormitoryManager(req,resp);
		}
		if("DormitoryManagerList".equals(method)){
			getDormitoryManagerListList(req,resp);
		}
		if("EditDormitoryManager".equals(method)){
			editEditDormitoryManager(req,resp);
		}
		if("DeleteDormitoryManager".equals(method)){
			deleteDeleteDormitoryManager(req,resp);
		}
	}

	private void deleteDeleteDormitoryManager(HttpServletRequest req,
			HttpServletResponse resp) {
		// TODO Auto-generated method stub
		String[] ids = req.getParameterValues("ids[]");
		DepartmentManagerDao departmentManagerDao = new DepartmentManagerDao();
		String msg = "";
		if(departmentManagerDao.delete(ids)){
			msg = "success";
		}
		departmentManagerDao.closeConnection();
		try {
			resp.getWriter().write(msg);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	private void editEditDormitoryManager(HttpServletRequest req,
			HttpServletResponse resp) {
		// TODO Auto-generated method stub
		Integer id = StringUtil.isEmpty(req.getParameter("id")) ? 0 : Integer.parseInt(req.getParameter("id"));
		String sn = req.getParameter("sn");
		String name = req.getParameter("name");
		String password = req.getParameter("password");
		String sex = req.getParameter("sex");
		DepartmentManager departmentManager = new DepartmentManager();
		departmentManager.setId(id);
		departmentManager.setName(name);
		departmentManager.setSex(sex);
		departmentManager.setPassword(password);
		departmentManager.setSn(sn);
		DepartmentManagerDao departmentManagerDao = new DepartmentManagerDao();
		String msg = "";
		if(departmentManagerDao.update(departmentManager)){
			msg = "success";
		}
		departmentManagerDao.closeConnection();
		try {
			resp.getWriter().write(msg);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	private void getDormitoryManagerListList(HttpServletRequest req,
			HttpServletResponse resp) {
		// TODO Auto-generated method stub
		String from = req.getParameter("from");
		//如果来自下拉框查询
		if("combox".equals(from)){
			returnByCombox(req,resp);
			return;
		}
		int pageNumber = Integer.parseInt(req.getParameter("page"));
		int pageSize = Integer.parseInt(req.getParameter("rows"));
		String name = req.getParameter("name");
		
		if(StringUtil.isEmpty(name)){
			name = "";
		}
		Map<String, Object> ret = new HashMap<String, Object>();
		DepartmentManagerDao departmentManagerDao = new DepartmentManagerDao();
		Page<DepartmentManager> page = new Page<DepartmentManager>(pageNumber, pageSize);
		page.getSearchProperties().add(new SearchProperty("name", "%"+name+"%", Operator.LIKE));
		//判断当前用户是否是宿管
		int userType = Integer.parseInt(req.getSession().getAttribute("userType").toString());
		if(userType == 3){
			//如果是宿管，则只能查看他自己的信息
			DepartmentManager loginedDormitoryManager = (DepartmentManager)req.getSession().getAttribute("user");
			page.getSearchProperties().add(new SearchProperty("id", loginedDormitoryManager.getId(), Operator.EQ));
		}
		Page<DepartmentManager> findList = departmentManagerDao.findList(page);
		ret.put("rows", findList.getConten());
		ret.put("total", findList.getTotal());
		departmentManagerDao.closeConnection();
		resp.setCharacterEncoding("utf-8");
		try {
			resp.getWriter().write(JSONObject.fromObject(ret).toString());
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	private void returnByCombox(HttpServletRequest req, HttpServletResponse resp) {
		// TODO Auto-generated method stub
		DepartmentManagerDao departmentManagerDao = new DepartmentManagerDao();
		Page<DepartmentManager> page = new Page<DepartmentManager>(1, 9999);
		//判断当前用户是否是宿管
		int userType = Integer.parseInt(req.getSession().getAttribute("userType").toString());
		if(userType == 3){
			//如果是宿管，则只能查看他自己的信息
			DepartmentManager loginedDormitoryManager = (DepartmentManager)req.getSession().getAttribute("user");
			page.getSearchProperties().add(new SearchProperty("id", loginedDormitoryManager.getId(), Operator.EQ));
		}
		page = departmentManagerDao.findList(page);
		departmentManagerDao.closeConnection();
		resp.setCharacterEncoding("utf-8");
		try {
			resp.getWriter().write(JSONArray.fromObject(page.getConten()).toString());
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	private void addDormitoryManager(HttpServletRequest req,
			HttpServletResponse resp) throws IOException {
		// TODO Auto-generated method stub
		String name = req.getParameter("name");
		String password = req.getParameter("password");
		String sex = req.getParameter("sex");
		resp.setCharacterEncoding("utf-8");
		if(StringUtil.isEmpty(name)){
			resp.getWriter().write("姓名不能为空!");
			return;
		}
		if(StringUtil.isEmpty(password)){
			resp.getWriter().write("密码不能为空!");
			return;
		}
		if(StringUtil.isEmpty(sex)){
			resp.getWriter().write("性别不能为空!");
			return;
		}
		DepartmentManager departmentManager = new DepartmentManager();
		departmentManager.setName(name);
		departmentManager.setPassword(password);
		departmentManager.setSex(sex);
		departmentManager.setSn(StringUtil.generateSn("DM", ""));
		DepartmentManagerDao departmentManagerDao = new DepartmentManagerDao();
		String msg = "添加失败!";
		if(departmentManagerDao.add(departmentManager)){
			msg = "success";
		}
		departmentManagerDao.closeConnection();
		resp.getWriter().write(msg);
	}
}
