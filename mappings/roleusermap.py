<?php


if(isset($_GET['specific_role'])):


	$role_id = isset($_GET['role_id']) ? $fieldValidator->validate_field($_GET['role_id']) : "";

	$userrolemap_array = array();
	$role_array = array();
	$user_array = array();

	$query = $queryExecutor->execute($selectionObj->select_role($role_id));

	while($row = mysqli_fetch_array($query)):

		$role_id = $row['role_id'];
		$role_array[$role_id] = array();
		$role_array[$role_id]['role_id'] = $role_id;

		$key = $role_id;

		$dependent_query = $queryExecutor->execute($selectionObj->select_role_name($role_id));
		$row_col = mysqli_fetch_array($dependent_query);
		$role_array[$key]['name'] = $row_col['name'];

		$dependent_query = $queryExecutor->execute($selectionObj->select_role_description($role_id));
		$row_col = mysqli_fetch_array($dependent_query);
		$role_array[$key]['description'] = $row_col['description'];


		$secondary_query = $queryExecutor->execute($selectionObj->select_userrolemap_by_role($role_id));

		while($sec_row = mysqli_fetch_array($secondary_query)):

			$user_id = $sec_row['user_id'];
			$user_array[$user_id] = array();
			$user_array[$user_id]['user_id'] = $user_id;

			$sec_key = $user_id;

			$dependent_query = $queryExecutor->execute($selectionObj->select_user_first_name($user_id));
			$row_col = mysqli_fetch_array($dependent_query);
			$user_array[$sec_key]['first_name'] = $row_col['first_name'];

			$dependent_query = $queryExecutor->execute($selectionObj->select_user_last_name($user_id));
			$row_col = mysqli_fetch_array($dependent_query);
			$user_array[$sec_key]['last_name'] = $row_col['last_name'];

			$dependent_query = $queryExecutor->execute($selectionObj->select_user_email($user_id));
			$row_col = mysqli_fetch_array($dependent_query);
			$user_array[$sec_key]['email'] = $row_col['email'];

			$dependent_query = $queryExecutor->execute($selectionObj->select_user_password($user_id));
			$row_col = mysqli_fetch_array($dependent_query);
			$user_array[$sec_key]['password'] = $row_col['password'];

			$dependent_query = $queryExecutor->execute($selectionObj->select_user_job_title($user_id));
			$row_col = mysqli_fetch_array($dependent_query);
			$user_array[$sec_key]['job_title'] = $row_col['job_title'];

		endwhile;



	endwhile;


?>

<table cellspacing = "1" cellpadding = "0" align = "center" width = "100%" id = "userrolemap">
 <tr>
 <td colspan = "7">&nbsp;&nbsp;&nbsp;&nbsp;</td>
 <td colspan = "2"><a href="target_print.php?userrolemap&&role_id=<?= $role_id ?>" target="_blank" style="color:#00FF00;">Print PDF</a></td></tr>
 <tr class = "top_row">
 <td>&nbsp;&nbsp;#&nbsp;&nbsp;</td>
 <td>&nbsp;User id&nbsp;</td>
 <td>&nbsp;First name&nbsp;</td>
 <td>&nbsp;Last name&nbsp;</td>
 <td>&nbsp;Email&nbsp;</td>
 <td>&nbsp;Password&nbsp;</td>
 <td>&nbsp;Job title&nbsp;</td>
 <td>&nbsp;Workspace id&nbsp;</td>
 <td>&nbsp;&nbsp;Actions&nbsp;&nbsp;</td></tr>
 
<?php $i = 0; ?>


<?php  foreach($user_array as $user_key => $user_value): ?>
<?php $css_class = ($i+1)%2 == 0 ? "even_row" : "odd_row"; ?>


<tr>
	<td><?= ($i+1) ?></td>
	<td><?= $user_value['user_id'] ?></td>
	<td><?= $user_value['first_name'] ?></td>
	<td><?= $user_value['last_name'] ?></td>
	<td><?= $user_value['email'] ?></td>
	<td><?= $user_value['password'] ?></td>
	<td><?= $user_value['job_title'] ?></td>
	<td><?= $user_value['workspace_id'] ?></td>
	<td>

		<?php $id_string = $user_id; ?>

		<div id="update_user_<?= $id_string ?>" style="display:none" class="updates">
		<table border="0" align="center" class="overlay_contained_table">
		<tr>
			<td align="right">
			<div class="closebtn" id="close_circle" onclick="closeUpdateOverlay('update_user_<?= $id_string ?>');">&nbsp;&times;&nbsp;</div>
			</td>
		</tr>
		<tr><td><br /></td></tr>
		<tr>
			<td align="center">
			<fieldset style="width: 80%">
			<legend>user Information</legend>
			<?php update_user($queryExecutor, $selectionObj, $updateObj, $fieldValidator, $user_value['user_id']); ?>
			</fieldset>
			</td>
		</tr>
		<tr>
			<td><br /></td>
		</tr>
		</table>
		</div>


<?php

	$userrolemap_count = count_userrolemap($queryExecutor, $selectionObj);
	$mapping_link = "userrolemap.php?user&&user_id=".$user_value['user_id']."";
	$title = "userrolemap corresponding entries.";
	$label = "Use.";
	get_mapping_mark_up($userrolemap_count, $mapping_link, $title, $label);

	$userstepmap_count = count_userstepmap($queryExecutor, $selectionObj);
	$mapping_link = "userstepmap.php?user&&user_id=".$user_value['user_id']."";
	$title = "userstepmap corresponding entries.";
	$label = "Use.";
	get_mapping_mark_up($userstepmap_count, $mapping_link, $title, $label);



?>


	<label id="update_link_<?= $id_string ?>" onclick="showUpdate('update_<?= $id_string ?>');" style="cursor:pointer">
	<img src="images/icons/edit.png" width="15px" height="15px" title="edit entry" style="cursor:pointer" />
	</label> 
 &nbsp; 
	<?php 
		$link = "user.php?delete_User&&user_id=".$user_value['user_id']."";
		$message = "";
	?>

	<?php showConfirmDeleteAction($id_string, $link, $message); ?>
	<label style="cursor:pointer" onclick="showDelete('delete_<?= $id_string ?>')">
	<img src="images/icons/delete.png" width="15px" height="15px" title="delete entry" />
	</label>
	</td>
<tr>
	<?php $i = ($i + 1); ?>
<?php endforeach; ?>
 <tr>
 <td colspan = "9"></td></tr></table>

<?php endif; ?>

